#include <stdio.h>
#include <cs50.h>
#include <math.h>

float positive_float(void);

int main(void)
{
    int total = round(positive_float() * 100);
    int coins = 0;

    // Inicio do programa
    do
    {
        // Verifica se ainda é possivel subtrair 0.25 centavos ou 25 e soma ao contador de vezes
        if (total - 25 >= 0)
        {
            total = total - 25;
            coins++;
        }
        // Verifica se ainda é possivel subtrair 0.10 centavos ou 10 e soma ao contador de vezes
        else if (total - 10 >= 0)
        {
            total = total - 10;
            coins++;
        }
        // Verifica se ainda é possivel subtrair 0.05 centavos ou 5 e soma ao contador de vezes
        else if (total - 5 >= 0)
        {
            total = total - 5;
            coins++;
        }
        // Verifica se ainda é possivel subtrair 0.01 centavos ou 1 e soma ao contador de vezes
        else
        {
            total = total - 1;
            coins++;
        }
    }
    while (total > 0);

    printf("%i\n", coins);

}

// Pergunta o valor e fica repetindo até que seja inserido um valor positivo
float positive_float(void)
{
    float number;
    do
    {
        number = get_float("Troca devida: ");
    }
    while (number < 0);
    return number;
}