
# -*- coding: utf-8 -*-
"""
Created on 09/06/17

@author: Genilton Cleiton
"""
'''
entrada = list(map(int, input().split(' ')))
temp = 0
saida = []
for i in range(len(entrada)):
    if entrada[i] == max(entrada):
        saida.append(i)
'''


class Pilha():
    def __init__(self):
        self.itens = []

    def vazia(self):
        return self.itens == []
    def topo(self):
        return self.itens(len(self.itens)-1)
    def tamanho(self):
        return len(self.itens)
    def empilha(self, e):
        self.itens.append(e)
        return
    def desempilha(self):
        self.itens.pop()
        return

def verifica(exp):
    p = Pilha()
    for i in exp:
        if i == '(':
            p.empilha(i)
        else:
            if p.vazia():
                return False
            else:
                p.desempilha()
    if p.vazia():
        return True
    else:
        return False


