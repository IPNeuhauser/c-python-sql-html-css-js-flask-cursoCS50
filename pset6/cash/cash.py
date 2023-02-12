from cs50 import get_float

def main():
    while True:
        cash = get_float("Change owned: ")
        if cash >= 0:
            break

    coins = 0
    cash = int(cash * 100)

    while cash > 0:
        if cash - 25 >= 0:
            cash -= 25
            coins += 1
        elif cash - 10 >= 0:
            cash -= 10
            coins += 1
        elif cash - 5 >= 0:
            cash -= 5
            coins += 1
        elif cash - 1 >= 0:
            cash -= 1
            coins += 1

    print(coins)

main()