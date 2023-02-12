#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Contante com a pontuação do jogo.
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Solicita as duas palavras.
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Pontuação das duas palavras, executa a função abaixo.
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Imprime quem venceu.
    if(score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string word)
{
    // Pega a palavra jogada e faz o cálculo da pontuação, retornando um valor inteiro.
    int value = 0;

    // Verifica caractere a caractere da palavra.
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        // Se o caractere for uma letra maiúscula transforma o mesmo em minúscula.
        if(isupper(word[i]))
        {
            word[i] += 32;
        }

        // Se o caractere for uma letra subtrai 97 dele e encontra o valor correspondente a letra na constante pontos.
        // Considerando que o valor da letra "a" está localizada no array[0] e o valor de "z" no array[26], ao subtrairmos 97 (valor ASCII da letra "a"), encontramos seu respectivo valor na variável POINTS
        if (isalpha(word[i]))
        {
            value += POINTS[word[i] - 97];
        }
        // Se não for uma letra, soma 0 ao score.
        else
        {
            value += 0;
        }
    }

    // retorna a pontuação total da palavra, que posteriormente será atribuida ao score 1 ou 2.
    return value;
}