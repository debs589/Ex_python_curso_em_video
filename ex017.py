"""Crie um programa que leia o comprimento do cateto
oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa"""

import math

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

print ('O valor da hipotenusa é: {:.2f}'.format(math.sqrt((co**2)+(ca**2))))