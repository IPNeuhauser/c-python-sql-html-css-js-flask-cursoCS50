#include <stdio.h>
#include <string.h>
#include <cs50.h>

int main (void)
{
    int digitos = 0, palavras = 1, frases = 0;
    float l = 0, s = 0, indice = 0;

    // solicita ao usuário o texto.
    string text = get_string("Text: ");

    // Corre sobre o texto analizando letra a letra para saber a onde armazenar a mesma.
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        // 1º if: se o digito estiver entre "a" e "z" maiusculo ou minusculo, adiciona 1 a váriavel digitos.
        if ((text[i] >= 'a' && text[i] <= 'z') || (text[i] >= 'A' && text[i] <= 'Z'))
        {
            digitos++;
        }
        // 2º if: se o digito for um " ", ele conta como se fosse uma palavra.
        // Adendo, a variável "palavras" começa com o valor = a 1 pois a ultima palavra não tem um espaço após.
        else if (text[i] == ' ')
        {
            palavras++;
        }
        // 3º if: Se o digito for um sinal gráfico de finalização de frases (! . ?), adiciona-se 1 a variável "frases".
        else if (text[i] == '!' || text[i] == '.' || text[i] == '?')
        {
            frases++;
        }
    }

    // Regra de 3 para descobrir a média de digitos e frases para um texto de 100 palavras.
    l = (float) (digitos * 100) / palavras;
    s = (float) (frases * 100) / palavras;

    // Cálculo do indice por meio do calculo de Coleman-Liau.
    indice = 0.0588 * l - 0.296 * s - 15.8;

    // Váriavel para arredondamento
    int inteiro = indice;

    // 1º if: Se o numero inteiro for maior que 1 e menor que 16 e os decimais da conta for maior que 0.5.
    if(indice - inteiro >= 0.5 && inteiro > 1 && inteiro < 16)
    {
        printf("Grade %i\n", inteiro + 1);
    }
    // 2º if: Se o numero inteiro for maior que 1 e menor que 16 e os decimais da conta for menor que 0.5.
    else if(indice - inteiro < 0.5 && inteiro > 1 && inteiro < 16)
    {
        printf("Grade %i\n", inteiro);
    }
    // 3º if: se o numero inteiro for menor que 1.
    else if(inteiro < 1)
    {
        printf("Before Grade 1\n");
    }
    // 4º if: se o numero inteiro for maior que 16.
    else if(inteiro > 16)
    {
        printf("Grade 16+\n");
    }
}