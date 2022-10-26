import csv



#l = input("insira o nome do arquivo com sua extensao: ")



lista = []
with open('dados.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for linha in spamreader:
        lista.append(linha)




# vamos criar uma função de 'busca'
def encontrar_pessoa(elemento):
    pos_i = 0 # variável provisória de índice
    pos_j = 0 # idem

    for i in range (len(lista)): # procurar em todas as listas internas
        for j in range (i): # procurar em todos os elementos nessa lista
            if elemento in lista[i][j]: # se encontrarmos elemento ('ana')
                pos_i = i # guardamos o índice i
                pos_j = j # e o índice j
                break # saímos do loop interno
            break # e do externo
    return (pos_i, pos_j) # e retornamos os índices


procura_pessoa = input("digite o nome da pessoa que deseja procurar: ") 


r = encontrar_pessoa(procura_pessoa) # chamamos a função e salvamos em r

















print(r) # imprime índices



print(lista[r[0]][r[1]]) # usa índices na lista como prova











