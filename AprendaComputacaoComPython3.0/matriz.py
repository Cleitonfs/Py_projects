# -*- coding: utf-8 -*-
"""
Created on  13/06/17

@author: Genilton Cleiton
"""

def cria_matriz(num_linhas, num_colunas):
    '''(int, int) -> matriz (lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas
    colunas em que cada elemento é digitado pelo usuário'''

    matriz = [] #lista vazia
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input('Digite o elemento [' + str(i) + '][' + str(j) + ']: '))
            linha.append(valor)

        matriz.append(linha)

    return matriz


def ler_matriz():
    lin = int(input('Digite o número de linhas da matriz: '))
    col = int(input('Digite o número de linhas da matriz: '))
    return cria_matriz(lin, col)


print(ler_matriz())
