# -* coding: utf-8 -*-
#
# Program to Calc angle between 2 vectors
#
# João Carlos Pandolfi Santana (C) - 2017
# Julian (c) - 2017
#
#
#  ->Usage:
#
# import algoritmo_calculo_vetores as alg
#
# va = alg.read_vector()
# vb = alg.read_vector()
#
# angle = alg.calc_angle_vector(va,vb)
#
#
#  ->Or Use:
# main()
#
###############################################


import math
import os
import random

print("esse programa esta escrito da seguinte forma: va = [x,y] e vb = [x2,y2]")


# ================== FUNCTIONS ===============

def read_vector():
    '''
        Function to read by interruption
        @returns vector {X,Y,Z,O,D}
    '''
    vector = float (input("Insira o vetor no formato: X,Y,Z,O,D ==> "))

    result = []

    for elem in vector:
        result.append(float(elem))

    return result


def calc_angle_vector(va, vb):
    '''
        Function calc angle between 2 vectores
        @receives va {x,y,z,a,b}
        @receives vb {x,y,z,a,b}
        @returns angle {Float}
    '''
    x_2 = va[0] * vb[0]
    y_2 = va[1] * vb[1]
    z_2 = va[2] * vb[2]
    o_2 = va[3] * vb[3]
    d_2 = va[4] * vb[4]
    umb = ((x_2) + (y_2) + (z_2) + (o_2) + (d_2))
    mva = (((x_2) + (y_2) + (z_2) + (o_2) + (d_2)) ** 0.5)
    mvb = (((vb[0] * vb[0]) + (vb[1] * vb[1]) + (vb[2] * vb[2]) + (vb[3] * vb[3]) + (vb[4] * vb[4])) ** 0.5)
    cos = (umb / (mvb * mva))
    acos = math.acos(cos)
    ang = ((acos * 180) / math.pi)

    return ang;


# print (va,vb,umb,mva,mvb,cos,acos,ang)

# controle = input("continuar ? s/n  ")

# ============== MAIN ================

def main():
    #
    controle = "s"
    #
    while controle == ("s"):
        print("VETOR A")
        va = read_vector()

        print("VETOR B")
        vb = read_vector()

        angle = calc_angle_vector(va, vb)

        print("RESULTADO: ", angle)

        controle = str(input("continuar ? s/n  "))


# ========= CALLING ========

main()