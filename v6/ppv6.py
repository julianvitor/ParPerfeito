#coding: utf-8

import csv
import math

# Função para abrir o banco de dados
def abrir_banco_dados():
    lista = []
    with open('/home/julian/Dev/ParPerfeito/v6/dados.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for linha in spamreader:
            lista.append(linha)
    return lista

# Função para encontrar uma pessoa no banco de dados
def encontrar_pessoa(nome, lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if nome in lista[i][j]:
                return i, j

# Função para calcular as combinações
def calcular_combinacoes(pessoa_procurada, valores_pessoa_procurada, lista):
    resultados = []
    for i in range(len(lista)):
        valores_pessoa = [float(lista[i][j]) for j in range(3, 26)]

        produto_escalar = sum(valores_pessoa_procurada[j] * valores_pessoa[j] for j in range(0, 23))
        modulo_vetor_pessoa_procurada = math.sqrt(sum(valores_pessoa_procurada[j] * valores_pessoa_procurada[j] for j in range(0, 23)))
        modulo_vetor_pessoa = math.sqrt(sum(valores_pessoa[j] * valores_pessoa[j] for j in range(0, 23)))

        cosseno = produto_escalar / (modulo_vetor_pessoa * modulo_vetor_pessoa_procurada)
        cosseno = min(1, cosseno)
        angulo = (math.acos(cosseno) * 180) / math.pi
        nome_par = lista[i][0]
        orientacao = int(lista[i][2])

        if orientacao == 1:
            orientacao = "hetero"
        elif orientacao == 2:
            orientacao = "bi"
        elif orientacao == 3:
            orientacao = "homosexual"

        resultados.append(f"{angulo},{pessoa_procurada} .=>. {orientacao} .<=>. {nome_par}.=>. {orientacao}")

    return resultados

# Função para salvar os resultados em um arquivo
def salvar_resultados(resultados):
    with open('/home/julian/Dev/ParPerfeito/v6/resultado.csv', 'w') as result_file:
        for res in resultados:
            result_file.write(res + "\n")

def main():
    lista = abrir_banco_dados()

    nome_pessoa_procurada = input("Digite o nome da pessoa que deseja procurar: ")
    pessoa_encontrada = encontrar_pessoa(nome_pessoa_procurada, lista)
    indice_lista_interna = pessoa_encontrada[0]
    total_pessoas = len(lista)

    print(f"Pessoa encontrada: {pessoa_encontrada}")
    print(f"Índice da lista interna: {indice_lista_interna}")
    print(f"Preferência: {lista[0][2]}")
    print(f"Total de pessoas: {total_pessoas}")
    print(f"Preferência: {lista[indice_lista_interna][2]}")

    valores_pessoa_procurada = [float(lista[indice_lista_interna][j]) for j in range(3, 26)]

    print(f"Valores da pessoa procurada: {valores_pessoa_procurada}")

    resultados = calcular_combinacoes(nome_pessoa_procurada, valores_pessoa_procurada, lista)
    salvar_resultados(resultados)

    print("Arquivo resultado.csv gerado com sucesso!")
    print("Estou te observando")

if __name__ == "__main__":
    main()
