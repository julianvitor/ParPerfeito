import csv
import math

class Pessoa:
    def __init__(self, dados):
        self.nome = dados[0]
        self.orientacao = int(dados[2])
        self.valores = [float(valor) for valor in dados[3:]]

    def calcular_similaridade(self, outra_pessoa):
        produto_escalar = sum(a * b for a, b in zip(self.valores, outra_pessoa.valores))
        modulo_self = math.sqrt(sum(a * a for a in self.valores))
        modulo_outra = math.sqrt(sum(b * b for b in outra_pessoa.valores))
        cosseno = produto_escalar / (modulo_self * modulo_outra)
        cosseno = min(1, cosseno)
        angulo = (math.acos(cosseno) * 180) / math.pi
        return angulo

    def obter_orientacao(self):
        if self.orientacao == 1:
            return "hetero"
        elif self.orientacao == 2:
            return "bi"
        elif self.orientacao == 3:
            return "homosexual"

class GerenciadorPessoas:
    def __init__(self):
        self.pessoas = []

    def carregar_dados(self, caminho_arquivo):
        with open(caminho_arquivo, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for linha in spamreader:
                pessoa = Pessoa(linha)
                self.pessoas.append(pessoa)

    def encontrar_pessoa(self, nome):
        for pessoa in self.pessoas:
            if nome in pessoa.nome:
                return pessoa

    def calcular_combinacoes(self, pessoa_procurada):
        resultados = []
        for pessoa in self.pessoas:
            if pessoa != pessoa_procurada:
                angulo = pessoa_procurada.calcular_similaridade(pessoa)
                orientacao_procurada = pessoa_procurada.obter_orientacao()
                orientacao_outra = pessoa.obter_orientacao()
                resultados.append(f"{angulo},{pessoa_procurada.nome} .=>. {orientacao_procurada} .<=>. {pessoa.nome}.=>. {orientacao_outra}")
        return resultados

    def salvar_resultados(self, resultados, caminho_arquivo):
        with open(caminho_arquivo, 'w') as result_file:
            for res in resultados:
                result_file.write(res + "\n")

    def processar(self, nome_pessoa_procurada, caminho_arquivo_dados, caminho_arquivo_resultado):
        self.carregar_dados(caminho_arquivo_dados)
        pessoa_procurada = self.encontrar_pessoa(nome_pessoa_procurada)
        resultados = self.calcular_combinacoes(pessoa_procurada)
        self.salvar_resultados(resultados, caminho_arquivo_resultado)
        print("Arquivo resultado.csv gerado com sucesso!")

if __name__ == "__main__":
    gerenciador = GerenciadorPessoas()
    nome_pessoa_procurada = input("Digite o nome da pessoa que deseja procurar: ")
    caminho_arquivo_dados = '/home/julian/Dev/ParPerfeito/v4/dados.csv'
    caminho_arquivo_resultado = '/home/julian/Dev/ParPerfeito/v4/resultado.csv'
    gerenciador.processar(nome_pessoa_procurada, caminho_arquivo_dados, caminho_arquivo_resultado)
