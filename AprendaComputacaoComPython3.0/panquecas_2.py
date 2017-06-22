# -*- coding: utf-8 -*-
"""
Created on  

@author: Genilton Cleiton
"""
entrada = list(map(int, input().split(' ')))

#entrada = [5, 4, 3, 2, 1]
cont = 0
saida_temp = []

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
        for i in range(len(temp)):
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

def virada(lista, indicebase):
    aux = lista[:]
    k = 0
    while indicebase >= 0:
        aux[k] = lista[indicebase]
        indicebase = indicebase - 1
        k = k + 1
    return aux

while cont < len(entrada)-1:
    posicaomaior = procuraindicemaior(entrada, cont)
    print(posicaomaior)
    saida_temp.append(posicaomaior[1]+1)
    virada(levaaotopo(entrada, posicaomaior[1]), len(entrada)-1-cont)
    cont+=1
    entrada_ordenada = sorted(entrada)
    lista_virada = (virada(levaaotopo(entrada, posicaomaior[1]), len(entrada)-1-cont))
    print(lista_virada)
    if  entrada == lista_virada:
        break

saida_temp.append(0)
str1 = ' '.join(str(e) for e in saida_temp)
#"" ".join(map(str, saida_temp))

print(str1)

"""   
print(procuraindicemaior(entrada, 1))
print(levaaotopo(entrada, 4))
print(virada(levaaotopo(entrada,4), 5))
"""



