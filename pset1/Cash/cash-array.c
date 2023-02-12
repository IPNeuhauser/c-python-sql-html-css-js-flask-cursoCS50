#include <stdio.h>
#include <math.h>
#include <cs50.h>

#define N 4
int valorCoins[N] = {25, 10, 5, 1};

int main (void)
{
    float input = 0;
    do
    {
        input = get_float("Valor: ");
    }
    while(input < 0);

    int valor = round(input * 100), moedas = 0;

    for(int i = 0; i < N && valor > 0; i++)
    {
        moedas += valor / valorCoins[i];
        valor = valor % valorCoins[i];
    }

    printf("%i\n", moedas);
}