"""Escreva um  programa que leia a velocidade de um carro

Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo
que ele foi multado.

A multa vai custar R$ 7,00 por cada Km acima do limite."""

veloc = float(input('Digite a velocidade do carro: '))

if veloc > 80:
    kmacima = veloc-80
    multa = kmacima*7
    print('Você ultrapassou o limite de 80 Km/h "\n"'
          'Km(s) acima do limite: {:.2f} "\n"'
          'Valor por cada Km acima do limite: {}"\n"'
          'Valor da multa: {:.2f}'.format(kmacima,'R$ 7,00',multa))
else:
    print('Velocidade dentro do limite de 80 Km/h')