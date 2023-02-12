#include <stdio.h>
#include <math.h>
#include <cs50.h>

int main(void)
{
     int popinicial, popfinal, anos = 0;
    do // Solicita ao usuário qual o valor inicial da população, não podendo ser inferior a 9
    {
        popinicial = get_int("Start size: ");
    }
    while(popinicial < 9);

    do // Solicita ao usuário qual o valor final da população, não podendo ser inferior ao valor inicial
    {
        popfinal = get_int("End size: ");
    }
    while(popfinal < popinicial);

    // Calcula o aumento populacional até que o mesmo seja maior ou igual ao valor da população final
    while(popinicial < popfinal)
    {
        popinicial = popinicial + (popinicial / 3) - (popinicial / 4);
        anos++;
    }

    // imprime na tela o valor de anos necessários para atingir tal crescimento populacional
    printf("Years: %i\n", anos);
}
