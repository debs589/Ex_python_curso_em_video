"""Faça um programa que leia a largura de uma
parede em metros, calcule a sua área e a
quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área
de 2m²."""


l = float (input('Digite a largura em metros: '))
a = float (input('Digite a altura em metros: '))

ar = l*a

print ('A quantidade de tinta necessária para pintar essa parede é de: {:.1f} L'.format(ar/2))