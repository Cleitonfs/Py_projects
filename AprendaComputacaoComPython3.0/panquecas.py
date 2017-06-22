# -*- coding: utf-8 -*-
"""
Created on  

@author: Genilton Cleiton
"""
#entrada = list(map(int, input().split(' ')))

entrada = [6,1,3,2,4,7]
def  procuraindicemaior (lista, k=0):
    indice = 0
    temp = []
    saida = []
    if lista[0] == max(lista):
        saida.append(max(lista))
        saida.append(0)
        return saida
    elif lista[len(lista)-1-k] == max(lista):
        indice = len(lista)-1-k
        saida.append(max(lista))
        saida.append(indice)
        return saida
    else:
        for i in range(len(lista)-k):
            temp.append(lista[i])
            maior = max(temp)
        for i in range(len(temp)-1):
            if temp[i] == maior:
                saida.append(maior)
                saida.append(i)
                break
    return saida

def levaaotopo(lista, indice):
    aux = lista[:]
    cont = 0
    while indice >= 0:
        aux[cont] = lista[indice]
        indice = indice-1
        cont = cont+1
    return aux




print(levaaotopo(entrada, 4))
print(procuraindicemaior(entrada, 4))
print(levaaotopo(entrada, 4))


'''
def rotacionasemipilha(lista, indice):
    if lista[0] == max(lista):
        lista_tmp = lista[:indice:-1]
        return lista_tmp
    elif

    elif lista[len(lista)-1-k] == max(lista):
        return indice
    if indice == len(lista) - 1:
        procuraindicemaior(lista, )
    lista_tmp = lista[:indice:-1]
    return lista_tmp
'''











