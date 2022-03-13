"""Escreva um programa que pergunte o salário de
um funcionário e calcule o valor de seu aumento.

Para salários superiores a R$ 1.250,00, calcule
um aumento de 10%

Para os inferiores ou iguais, o aumento é de 15%"""

salario = float(input('Digite o seu salário: '))

if salario > 1250:
    aumento = salario * 1.1
    print('Seu novo salário com aumento é de: R$ {:.2f}'.format(aumento))
else:
    aumento = salario * 1.15
    print('Seu novo salário com aumento é de: R$ {:.2f}'.format(aumento))