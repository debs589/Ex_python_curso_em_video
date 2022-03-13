"""Faça um programa que leia três números e mostre qual
é o maior e qual é o menor"""


n1 = float(input('Digite o número 1: '))
n2 = float(input('Digite o número 2: '))
n3 = float(input('Digite o número 3: '))

if n1 > n2 and n1 > n3:
    print('O Maior número inserido é: {}'.format(n1))
else:
    if n2 > n1 and n2 > n3:
        print('O Maior número inserido é: {}'.format(n2))
    else:
            print('O Maior número inserido é: {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('O Menor número inserido é: {}'.format(n1))
else:
    if n2 < n1 and n2 < n3:
        print('O Menor número inserido é: {}'.format(n2))
    else:
            print('O Menor número inserido é: {}'.format(n3))


