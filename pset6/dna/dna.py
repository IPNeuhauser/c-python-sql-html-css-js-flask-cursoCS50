import sys
import csv

def main():
    # Verifica se foi digitado o número de argumentos necessários
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # Cria uma lista chamada baseDados onde armazena todas as informações do arquivo
    baseDados = []
    with open(sys.argv[1], "r") as file:
        leitor = csv.DictReader(file)
        # Adiciona (append) cada linha a base de dados
        for row in leitor:
            baseDados.append(row)

    # Lê a sequencia que temos que analisar
    with open(sys.argv[2], "r") as file:
        sequencia = file.read()

    # Cria uma lista baseada nos titulos(keys) do banco de dados
    subSequencias = list(baseDados[0].keys())[1:] #[1:] diz que queremos começar do item 1 ao inves do 0 nesta lista

    # Cria uma variável dicionário para armazenar os resultados.
    resultados = {}

    # Para cada valor da variavel subSequencias. O nome subSequencia pode ser qualquer nome pois só representa cada valor na outra variável.
    for subSequencia in subSequencias:
        # Armazena o valor encontrado na função na variável resultados, relacionando ao nome em que foi buscado.
        resultados[subSequencia] = maiorSequencia(sequencia, subSequencia)

    # Para cada valor na variável baseDados.
    for pessoa in baseDados:
        sequenciasIguais = 0
        # Para cada valor presente em subSequencias, presente em baseDados
        for subSequencia in subSequencias:
            # Se o valor na baseDados for igual ao valor em resultados para a subsequencia buscada.
            if int(pessoa[subSequencia]) == resultados[subSequencia]:
                sequenciasIguais += 1
            else:
                break

        # Se o número de sequenciasIguais for o mesmo do total de sequencias analisadas, imprime o nome da pessoa.
        if sequenciasIguais == len(subSequencias):
            print(pessoa["name"])
            return

    # Caso não encontre uma pessoa, imprime que não tem compatibilidade.
    print("No match")

# A Função recebe como input a sequencia e os tipos de subSequencias a ser analisadas
def maiorSequencia(sequencia, subSequencia):
    maiorRepeticao = 0
    tamanhoSequencia = len(sequencia)
    tamanhoSubSequencia = len(subSequencia)

    # Para cada caracter na sequencia
    for i in range(tamanhoSequencia):
        contador = 0;

        # Enquanto for verdadeiro fica repetindo
        while True:
            # Define a posição inicial e final a ser analisada.
            inicio = i + contador * tamanhoSubSequencia
            fim = inicio + tamanhoSubSequencia

            # Se a sequencia nessa posição for igual a subSequencia analisada, continua repetindo, caso contrario sai do loop
            if sequencia[inicio:fim] == subSequencia:
                contador += 1
            else:
                break

            # Verifica se o número de iterações no loop é maior que a maiorRepetição anterior
            maiorRepeticao = max(maiorRepeticao, contador)

    return maiorRepeticao

main()