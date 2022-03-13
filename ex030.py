"""Crie um programa que leia um número inteiro e
mostre na tela se ele é PAR ou ÍMPAR."""

numero = int(input('Digite um número inteiro: '))

#Todo número par é divisível por 2, então se, o resto da divisão de um número por 2 for 0, ele é par

numero1 = numero%2

if numero1==0:
    print('O número {} é PAR'.format(numero))
else:
    print ('O número {} é ÍMPAR'.format(numero))