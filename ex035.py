"""Desenvolva um programa que leia o comprimento
de três retas e diga ao usuário se elas podem
ou não formar um triângulo."""


c1 = int(input('Digite o comprimento da primeira reta: '))
c2 = int(input('Digite o comprimento da segunda reta: '))
c3 = int(input('Digite o comprimento da terceira reta: '))

#Para formar um triângulo, a soma de 2 lados deve ser maior que o terceiro

if c1 + c2 > c3 and c1 + c3 > c2 and c2 + c3 > c1:
    print('As retas PODEM formar um triângulo')
else:
    print('As retas NÃO podem formar um triângulo')