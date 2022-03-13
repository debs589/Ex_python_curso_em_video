"""Faça um programa que leia um ano qualquer e mostre se
ele é BISSEXTO"""

ano = int(input('Digite um ano: '))

#Um ano bissexto é divisível por 4, então se, o resto da divisão de um ano por 4 for 0, ele é bissexto

if ano%4 ==0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} NÃO é bissesxto'.format(ano))