from cs50 import get_int

def main():
    cartao = solicitar()
    empresa = "INVALID"
    soma = somar(cartao[::-1])

    if soma == True:
        empresa = verificar(int(cartao[0:2]), int(len(cartao)))

    print(empresa)

def somar(cartao):
    count = 1
    soma = 0
    for c in cartao:
        if count % 2 == 1:
            soma += int(c)
            count += 1
        elif count % 2 == 0:
            soma += int((int(c) * 2) / 10) + (int(c) * 2) % 10
            count +=1

    if soma % 10 == 0:
        return True

    return False


def verificar(prefixo, digitos):
    if prefixo > 50 and prefixo < 56 and digitos == 16:
        return "MASTERCARD"
    elif (prefixo == 34 or prefixo == 37) and digitos == 15:
        return "AMEX"
    elif int(prefixo / 10) == 4 and (digitos == 13 or digitos == 16):
        return "VISA"
    else:
        return "INVALID"

def solicitar():
    while True:
        cartao = get_int("Number: ")
        if cartao > 0:
            break

    return str(cartao)

main()