#include <stdio.h>
#include <cs50.h>
#include <math.h>

long crednumb(void);

int main(void)
{
    // "cnum" salva o número inteiro para não precisar pedir novamente, "cc" salva o número para poder ser alterado
    long cnum = crednumb(), cc = cnum;

    // "n" é o dígito solicitado, as "somas" salvam as somas dos digitos solicitados, "ndigitos" salva a quantidade de digitos do cartão
    int n = 0, soma = 0, ndigitos = 0;

    do // Pega o valor do último dígito e soma na variável "somaimpar", após divide o número por 100 para ir ao próximo número
    {
        n = cc % 10;
        soma += n;
        cc = cc / 100;
    }
    while (cc > 0);

    cc = cnum / 10;

    do // Pega o valor dos dígitos pares de trás para a frente, multiplica por 2 e após a multiplicação pega o primeiro e ultimo dígito do resultado e soma
    {
        n = (cc % 10) * 2;
        soma += (n % 10) + (n / 10);
        cc = cc / 100;
    }
    while (cc > 0);

    cc = cnum;

    if (soma % 10 == 0)
    {
        do // Conta a quantidade de dígitos no cartão
        {
            cc = cc / 10;
            ndigitos++;
        }
        while (cc > 0);

        cc = cnum;

        for (long i = 0; i < ndigitos - 2; i++) // Reduz a quantidade de caracteres para 2 dígitos
        {
            cc = cc / 10;
        }

        // Verificação para saber se o cartão é master
        if (cc > 50 && cc < 56 && ndigitos == 16)
        {
            printf("MASTERCARD\n");
        }
        // Verificação para saber se o cartão é American Express
        else if ((cc == 34 || cc == 37) && ndigitos == 15)
        {
            printf("AMEX\n");
        }
        // Verificação para saber se o cartão é Visa
        else if (cc / 10 == 4 && (ndigitos == 13 || ndigitos == 16))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}

// Solicita o número do cartão até que seja fornecido um número positivo
long crednumb(void)
{
    long numb;
    do
    {
        numb = get_long("Digite o número do cartão: ");
    }
    while (numb <= 0);
    return numb;
}