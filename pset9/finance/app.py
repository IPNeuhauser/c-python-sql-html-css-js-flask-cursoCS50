import os
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    dados = db.execute("SELECT name, symbol, qntd, price FROM users JOIN owned ON user_id = id WHERE id = ?", session.get("user_id"))
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session.get("user_id"))
    cash = round(float(cash[0]['cash']), 2)
    return render_template("index.html", dados = dados, cash = cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol") or not request.form.get("shares") or int(request.form.get("shares")) < 1:
            return apology("Incomplete form!", 403)

        now = datetime.datetime.now()
        symbol = request.form.get("symbol")
        show = lookup(symbol)

        if show:
            qntd = request.form.get("shares")
            cash = db.execute("SELECT cash FROM users WHERE id = ?", session.get("user_id"))
            lisymbol = db.execute("SELECT symbol FROM owned WHERE user_id = ?", session.get("user_id"))

            cash[0]['cash'] = cash[0]['cash'] - (float(show['price']) * float(qntd))

            if cash[0]['cash'] < 0:
                return apology("You don't have money to buy this!", 403)

            count = 0
            exist = False

            while(count < len(lisymbol)):
                if symbol.upper() == lisymbol[count]['symbol']:
                    exist = True
                count += 1

            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash[0]['cash'], session.get("user_id"))
            db.execute("INSERT INTO transactions (user_id, symbol, qntd, price, date) VALUES (?, ?, ?, ?, ?)", session.get("user_id"), show['symbol'], qntd, round(show['price'], 2), now)

            if exist:
                quantidade = db.execute("SELECT qntd FROM owned WHERE symbol = ? AND user_id = ?", show['symbol'], session.get("user_id"))
                qntd = int(qntd) + int(quantidade[0]['qntd'])
                db.execute("UPDATE owned SET qntd = ? WHERE symbol = ? AND user_id = ?", qntd, show['symbol'], session.get("user_id"))
                db.execute("UPDATE owned SET price = ? WHERE symbol = ? AND user_id = ?", round(show['price'], 2), show['symbol'], session.get("user_id"))
            else:
                db.execute("INSERT INTO owned (user_id, name, symbol, qntd, price) VALUES (?, ?, ?, ?, ?)", session.get("user_id"), show['name'], show['symbol'], qntd, round(show['price'], 2))

            session['message'] = 'buy'
            return redirect("/")
    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    dados = db.execute("SELECT symbol, qntd, price, date FROM users JOIN transactions ON user_id = id WHERE id = ?", session.get("user_id"))
    session['message'] = ''
    return render_template("history.html", dados = dados)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        session['message'] = 'login'
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        nome = request.form.get("symbol")
        SHOW = lookup(nome)

        if len(SHOW) != 0:
            session['message'] = ''
            return render_template("quoted.html", show=SHOW)

        return apology("Solicitação invalida", 403)
    else:
        return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    """Register user"""
    if request.method == "POST":
        if not request.form.get("username") or not request.form.get("password") or not request.form.get("check") or request.form.get("password") != request.form.get("check"):
            return apology("Invalid form!", 403)

        usuarios = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(usuarios) != 1:
            nome = request.form.get("username")
            senha = generate_password_hash(request.form.get("password"))
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", nome, senha)
            session['message'] = 'register'
            row = db.execute("SELECT id FROM users WHERE username = ?", nome)
            session['user_id'] = row[0]['id']
            return redirect("/")
        else:
            return apology("Username already registered", 403)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        if not request.form.get("shares") or not request.form.get("symbol") or int(request.form.get("shares")) < 1:
            return apology("Inconplete Form", 403)

        qntd = request.form.get("shares")
        symbol = request.form.get("symbol")
        show = lookup(symbol)

        qntdSym = db.execute("SELECT qntd FROM owned WHERE symbol = ? and user_id = ?", symbol, session.get("user_id"))
        if qntdSym[0]['qntd'] < int(qntd):
            return apology("Saldo insuficiente!", 403)

        now = datetime.datetime.now()
        qntdSym = qntdSym[0]['qntd'] - float(qntd)
        valor = float(qntd) * float(show['price'])
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session.get('user_id'))
        cash = cash[0]['cash'] + valor

        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, session.get('user_id'))
        db.execute("INSERT INTO transactions(user_id, symbol, qntd, price, date) VALUES (?, ?, ?, ?, ?)", session.get('user_id'), show['symbol'], -int(qntd), show['price'], now)
        db.execute("UPDATE owned SET qntd = ? WHERE user_id = ? AND symbol = ?", qntdSym, session.get('user_id'), show['symbol'])
        session['message'] = 'sold'
        return redirect("/")
    else:
        dados = db.execute("SELECT symbol, qntd FROM owned WHERE user_id = ?", session.get("user_id"))
        return render_template("sell.html", dados=dados)


@app.route("/password", methods=["GET", "POST"])
@login_required
def password():

    if request.method == "POST":
        if not request.form.get('actual-password') or not request.form.get('password') or not request.form.get('check'):
            return apology("Invalid form!", 403)

        hash = db.execute("SELECT hash FROM users WHERE id = ?", session['user_id'])
        oldHash = request.form.get('actual-password')

        if check_password_hash(hash[0]['hash'], oldHash):
            newHash = request.form.get('password')
            checkHash = request.form.get('check')
            if newHash == checkHash and newHash != oldHash:
                db.execute("UPDATE users SET hash = ? WHERE id = ?", generate_password_hash(newHash), session['user_id'])
                session['message'] = 'password'
                return redirect("/")
            else:
                return apology("The new password don't match", 403)
        else:
            return apology("Invalid old password", 403)

    else:
        return render_template("password.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
