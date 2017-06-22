# -*- coding: utf-8 -*-
"""
Created on  

@author: Genilton Cleiton
"""
import math

def logaritmo(x):
    if x < 0:
        print("Somentes números positivos, por favor")
        return
    else:
        return print("O log de x é: ", math.log10(x))
logaritmo(100)

def contagemReg(n):
    if n == 0:
        return print("Fogo!")
    else:
        print(n)
        contagemReg(n-1)
