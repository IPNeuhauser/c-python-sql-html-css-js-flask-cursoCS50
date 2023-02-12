#include <stdio.h>
#include <cs50.h>

int positive_number(void);

int main(void)
{

    int control = positive_number();

    // Váriavel "y" escolhe a linha da pirâmide
    for(int y = 0; y < control; y++)
    {

            // Váriavel "control_space" imprime o número de " " necessários para fazer a pirâmide inverter
            int control_space = control - y - 1;
            while(control_space > 0)
            {
                printf(" ");
                control_space--;
            }

            // Váriavel "x" escolhe quantas vezes tem que repetir o "#" na linha
            for (int x = 0; x <= y; x++)
            {
                printf ("#");
            }

        printf ("\n");
    }

}

// solicita um numero inteiro entre 1 e 8
int positive_number (void)
{
    int number;
    do
    {
        number = get_int("Escreva um número entre 1 e 8: ");
    }
    while (number < 1 || number > 8);
    return number;
}