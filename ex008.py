"""Escreva um programa que leia um vaor em metros
e o exiba convertido em centímetros e milímetros"""


m = float (input ('Digite o valor em metros: '))
cm = m*100
mm = m*1000

print ('O valor em centímetros é: {:.2f} e em milímetros é: {:.2f}'. format(cm,mm))