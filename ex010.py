"""Crie um programa que leia quanto dinheiro uma
pessoa tem na carteira e mostre quantos dólares
ela pode comprar.

Considere
US$ 1.00 = R$ 3.27"""


n = float (input('Quantos reais você tem?: '))
d = n/3.27

print ('Você pode comprar {:.2f} dólar(es)'.format(d))