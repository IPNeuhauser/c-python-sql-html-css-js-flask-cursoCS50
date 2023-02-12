from cs50 import get_string

def main():
    texto = get_string("Text: ")

    palavras = 1
    frases = 0
    letras = 0

    for c in texto:
        if c == " ":
            palavras += 1
        elif c == "!" or c == "?" or c == ".":
            frases += 1
        elif c.lower() >= "a" and c.lower() <= "z":
            letras += 1

    l = (letras * 100) / palavras
    s = (frases * 100) / palavras

    indice = round(0.0588 * l - 0.296 * s - 15.8)

    if indice <= 1:
        print("Before Grade 1")
    elif indice >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {indice}")

main()