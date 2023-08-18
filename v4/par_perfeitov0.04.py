#coding: utf-8

import csv
import math


while True:
    lista = []
    #abrir banco de dados
    with open('/home/julian/Dev/ParPerfeito/v4/dados.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for linha in spamreader:
            lista.append(linha)

    #função de 'busca'
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





    #aqui comeca o mapeamento dos elementos

    procura_pessoa = input("digite o nome da pessoa que deseja procurar: ") 
    pessoa_endereco = encontrar_pessoa(procura_pessoa) # chamamos a funcao e salvamos em lista_pessoa_endereco
    lista_pessoa_endereco = list(pessoa_endereco)
    lista_interna = int(lista_pessoa_endereco[0])
    numero_pessoas = len(lista)

    print(lista_pessoa_endereco,"pessoa endereco")
    print(lista_interna,"lista interna")
    print(lista[0][2],"lista[0][2]")
    print(numero_pessoas,"numero de pessoas")
    print (lista[lista_interna][2],"preferencia")

    VA = [] #pessoa constante que foi definida pelo entry de entrada
    VB = [] #pessoas do banco de dados para combinar

    #variaveis do banco de dados
    a_preferencia = (lista[lista_interna][2])
    aa = (lista[lista_interna][3])
    ab = (lista[lista_interna][4])
    ac = (lista[lista_interna][5])
    ad = (lista[lista_interna][6])
    ae = (lista[lista_interna][7])
    af = (lista[lista_interna][8])
    ag = (lista[lista_interna][9])
    ah = (lista[lista_interna][10])
    ai = (lista[lista_interna][11])
    aj = (lista[lista_interna][12])
    ak = (lista[lista_interna][13])
    al = (lista[lista_interna][14])
    am = (lista[lista_interna][15])
    an = (lista[lista_interna][16])
    ao = (lista[lista_interna][17])
    ap = (lista[lista_interna][18])
    aq = (lista[lista_interna][19])
    ar = (lista[lista_interna][20])
    a_s = (lista[lista_interna][21])
    at = (lista[lista_interna][22])
    au = (lista[lista_interna][23])
    av = (lista[lista_interna][24])
    aw = (lista[lista_interna][25])

    a_preferencia = int(a_preferencia)
    aa = float(aa)
    ab = float(ab)
    ac = float(ac)
    ad = float(ad)
    ae = float(ae)
    af = float(af)
    ag = float(ag)
    ah = float(ah)
    ai = float(ai)
    aj = float(aj)
    ak = float(ak)
    al = float(al)
    am = float(am)
    an = float(an)
    ao = float(ao)
    ap = float(ap)
    aq = float(aq)
    ar = float(ar)
    a_s = float(a_s)
    at = float(at)
    au = float(au)
    av = float(av)
    aw = float(aw)
    
    #condicionais para expecificar na hora de ler as informacoes do arquivo final
    if (a_preferencia == 1):
        a_preferencia = ("hetero")
    elif (a_preferencia == 2):
        a_preferencia = ("bi")
    elif (a_preferencia == 3):
        a_preferencia = ("homosexual")



    #pessoa constante que foi definida pelo entry de entrada
    VA = [float(aa), float(ab), float(ac), float(ad), float(ae), float(af), float(ag), float(ah), float(ai), float(aj),
          float(ak), float(al), float(am), float(an), float(ao), float(ap), float(aq), float(ar), float(a_s), float(at),
          float(au), float(av), float(aw)]

    print(VA)


    #calculo para as combinacoes
    c = (0)
    results = []
    while c < numero_pessoas:

        c = (0 + c)

        ba = (lista[c][3])
        bb = (lista[c][4])
        bc = (lista[c][5])
        bd = (lista[c][6])
        be = (lista[c][7])
        bf = (lista[c][8])
        bg = (lista[c][9])
        bh = (lista[c][10])
        bi = (lista[c][11])
        bj = (lista[c][12])
        bk = (lista[c][13])
        bl = (lista[c][14])
        bm = (lista[c][15])
        bn = (lista[c][16])
        bo = (lista[c][17])
        bp = (lista[c][18])
        bq = (lista[c][19])
        br = (lista[c][20])
        b_s = (lista[c][21])
        bt = (lista[c][22])
        bu = (lista[c][23])
        bv = (lista[c][24])
        bw = (lista[c][25])

        ba = float(ba)
        bb = float(bb)
        bc = float(bc)
        bd = float(bd)
        be = float(be)
        bf = float(bf)
        bg = float(bg)
        bh = float(bh)
        bi = float(bi)
        bj = float(bj)
        bk = float(bk)
        bl = float(bl)
        bm = float(bm)
        bn = float(bn)
        bo = float(bo)
        bp = float(bp)
        bq = float(bq)
        br = float(br)
        b_s = float(b_s)
        bt = float(bt)
        bu = float(bu)
        bv = float(bv)
        bw = float(bw)

        VB = [(ba),(bb),(bc),(bd),(be), (bf), (bg),(bh),(bi),(bj),(bk),(bl),(bm),(bn),(bo),(bp),(bq),(br),(b_s),(bt),
              (bu),(bv),(bw)]

        umb = ((aa * ba) + (ab * bb) + (ac * bc) + (ad * bd) + (ae * be) + (af * bf) + (ag * bg) + (ah * bh) + (ai * bi) + (
        aj * bj) + (ak * bk) + (al * bl) + (am * bm) + (an * bn) + (ao * bo) + (ap * bp) + (aq * bq) + (ar * br) + (
               a_s * b_s) + (at * bt) + (au * bu) + (av * bv) + (aw * bw))

        mva = ((
               (aa * aa) + (ab * ab) + (ac * ac) + (ad * ad) + (ae * ae) + (af * af) + (ag * ag) + (ah * ah) + (ai * ai) + (
               aj * aj) + (ak * ak) + (al * al) + (am * am) + (an * an) + (ao * ao) + (ap * ap) + (aq * aq) + (ar * ar) + (
               a_s * a_s) + (at * at) + (au * au) + (av * av) + (aw * aw)) ** 0.5)

        mvb = ((
               (ba * ba) + (bb * bb) + (bc * bc) + (bd * bd) + (be * be) + (bf * bf) + (bg * bg) + (bh * bh) + (bi * bi) + (
               bj * bj) + (bk * bk) + (bl * bl) + (bm * bm) + (bn * bn) + (bo * bo) + (bp * bp) + (bq * bq) + (br * br) + (
               b_s * b_s) + (bt * bt) + (bu * bu) + (bv * bv) + (bw * bw)) ** 0.5)

        cos = (umb / (mvb * mva))
        if cos > 1:
            cos = 1
        print(cos)

        acos = math.acos(cos)
        ang = ((acos * 180) / math.pi)
        nome_par = (lista[c][0])
        orientacao = (lista[c][2])
        orientacao = int(orientacao)

        print(ang, " ", procura_pessoa, nome_par)

        c = (1 + c)

        if (orientacao == 1):
            orientacao = ("hetero")
        elif (orientacao == 2):
            orientacao = ("bi")
        elif (orientacao == 3):
            orientacao = ("homosexual")

        combinacoes = [str(ang) + " ==> " + str(procura_pessoa) + "<=>" + str(nome_par)]

        result_file = open('/home/julian/Dev/ParPerfeito/v4/resultado.csv', 'w')

        results.append(
            str(ang) + "," + str(procura_pessoa) + " .=>. " + str(a_preferencia) + str(" .<=>. ") + str(nome_par) + ".=>. " + str(orientacao))

        for res in results:
            result_file.write(res + "\n")
        result_file.close()

    print("arquivo gerado")







