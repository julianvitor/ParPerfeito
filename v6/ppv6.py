import csv
import math

class Pessoa:
    def __init__(self, dados):
        self.nome = dados[0]
        self.orientacao = int(dados[2])
        self.valores = [float(valor) for valor in dados[3:]]

    def calcular_produto_escalar(self, outra_pessoa):
        return sum(a * b for a, b in zip(self.valores, outra_pessoa.valores))

    def calcular_modulo(self):
        return math.sqrt(sum(a * a for a in self.valores))

    def calcular_angulo(self, cosseno):
        cosseno = min(1, cosseno)
        angulo = (math.acos(cosseno) * 180) / math.pi
        return angulo

    def calcular_similaridade(self, outra_pessoa):
        produto_escalar = self.calcular_produto_escalar(outra_pessoa)
        modulo_self = self.calcular_modulo()
        modulo_outra = outra_pessoa.calcular_modulo()
        cosseno = produto_escalar / (modulo_self * modulo_outra)
        return self.calcular_angulo(cosseno)

    def obter_orientacao(self):
        orientacoes = {1: "hetero", 2: "bi", 3: "homosexual"}
        return orientacoes.get(self.orientacao, "Desconhecido")

class GerenciadorPessoas:
    def __init__(self):
        self.pessoas = []

    def carregar_dados(self, caminho_arquivo):
        with open(caminho_arquivo, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for linha in csv_reader:
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
    caminho_arquivo_dados = '/home/julian/Dev/ParPerfeito/v6/dados_random.csv'
    caminho_arquivo_resultado = '/home/julian/Dev/ParPerfeito/v6/resultado.csv'
    gerenciador.processar(nome_pessoa_procurada, caminho_arquivo_dados, caminho_arquivo_resultado)
