"""Faça um algoritmo que leia o salário de um
funcionário e mostre seu novo salário, com
15% de aumento"""

salario = float(input('Digite o seu salário: '))
aumento = salario * 1.15

print('Seu salário com aumento é de: {:.2f}'.format(aumento))