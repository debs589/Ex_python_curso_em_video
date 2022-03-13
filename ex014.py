"""Escreva um programa que converta uma temperatura
digitada em °C e converta para °F"""

temp = float(input('Digite a temperatura em °C: '))
fahrenheit = 1.8 * temp + 32

print('A temperatura digitada é igual a {:.1f}°F'.format(fahrenheit))