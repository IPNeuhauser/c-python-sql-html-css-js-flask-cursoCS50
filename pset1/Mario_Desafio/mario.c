#include <stdio.h>
#include <cs50.h>

int positive_number(void);

int main(void)
{
    int altura = positive_number();

    // Váriavel "y" controla a altura da pirâmide
    for (int y = 0; y < altura; y++)
    {
        // Váriavel "control_space" controla a quantidade de " " necessários para inverter a pirâmide da esquerda
        int control_space = altura - y - 1;

        while (control_space > 0)
        {
            printf(" ");
            control_space--;
        }

        // Váriavel "x" controla a quantidade de "#" da pirâmide a direita
        for (int x = 0; x <= y; x++)
        {
            printf("#");
        }

        printf("  ");

        // Váriavel "xx" controla a quantidade de "#" da pirâmide a esquerda
        for (int xx = 0; xx <= y; xx++)
        {
            printf("#");
        }

        printf("\n");
    }

}

int positive_number(void)
{
    int number;
    do
    {
        number = get_int("Escolha um número entre 1 e 8: ");
    }
    while (number < 1 || number > 8);
    return number;
}