"""Faça um programa que leia uma frase pelo teclado
e mostre:"""

#1: Quantas vezes aparece a letra "A"

frase = str(input('Digite uma frase: '))

"""comando strip - tirar todos os espaços à direita e à esquerda
comando upper - deixar nome em maiúsculo
comando count - contar vezes que "A" aparece"""

frase1 = frase.strip().upper().count('A')
print('A letra "A" aparece {} vezes na frase'.format(frase1))

#2: Em que posição ela aparece a primeira vez

frase2 = frase.strip().upper().find('A')
print('A letra "A" aparece a primeira vez '
      'na frase na posição: {}'.format(frase2))

#3: Em que posição ela aparece a última vez