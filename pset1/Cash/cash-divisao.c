#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main (void)
{
   float valor = 0;
   do
   {
    valor = get_float("Valor: ");
   }
   while(valor < 0);

   int total = round(valor * 100);
   int moedas = 0;

   while(total > 0)
   {
    if(total/25 > 0)
    {
        moedas += total/25;
        total = total % 25;
    }
    else if(total/10 > 0)
    {
        moedas += total/10;
        total = total % 10;
    }
    else if(total/5 > 0)
    {
        moedas += total/5;
        total = total % 5;
    }
    else
    {
        moedas += total/1;
        total = total % 1;
    }
   }

   printf("%i\n", moedas);
}