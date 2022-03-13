"""Crie um programa que leia um número real
qualquer e mostre na tela a sua porção inteira"""

import math
n = float(input('Digite um número: '))
print ('A parte inteira do número digitado é: {}'.format(math.trunc(n)))
