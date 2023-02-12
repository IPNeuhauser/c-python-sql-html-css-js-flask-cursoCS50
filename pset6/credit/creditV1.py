from cs50 import get_int

def main():
    while True:
        number = get_int("Number: ")
        if number > 0:
            break

    cc = number
    soma = 0
    digitos = 0

    while int(cc) > 0:
        digitos += 1
        cc /= 10

    cc = number
    count = digitos

    while int(cc) > 0:
        digito = int(cc % 10)
        soma += digito
        cc = int(cc / 100)

    cc = int(number / 10)
    while int(cc) > 0:
        digito = int(cc % 10) * 2
        soma += digito % 10 + int(digito / 10)
        cc = int(cc / 100)

    count = digitos
    while count > 2:
        count -= 1
        number = int(number / 10)

    if soma % 10 == 0:
        if number > 50 and number < 56 and digitos == 16:
            print("MASTERCARD")
        elif (number == 34 or number == 37) and digitos == 15:
            print("AMEX")
        elif int(number / 10) == 4 and (digitos == 13 or digitos == 16):
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")

main()