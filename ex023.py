# Faça um programa que leia um número de 0 a 999
# e mostre na tela cada um dos dígitos separados

num = str(input('Digite um número de 0 até '
                   '9999: '))

print('unidade: {}'.format(num[0]))
print('dezena: {}'.format(num[1]))
print('centena: {}'.format(num[2]))
print('milhar: {}'.format(num[3]))
