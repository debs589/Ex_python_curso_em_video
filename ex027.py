"""Faça um programa que leia o nome completo de
uma pessoa, mostrando em seguida o primeiro e
o último nome, separadamente"""

nome = str(input('Digite seu nome completo: '))
nome1 = nome.strip().split()

#Comando Len para descobrir quantas palavras existem no nome completo
nome2 = len(nome1)

#A posição do último nome será o comprimento total do nome (qtde de palavras) -1
sobrenome = nome1[nome2-1]

print('Primeiro nome: {} ' "\n"
      'Último nome: {}'.format(nome1[0],sobrenome))