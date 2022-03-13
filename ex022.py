"""Crie um programa que leia o nome completo de uma pessoa
e mostre:"""

nome = input('Digite o seu nome completo: ')

# O nome com todas as letras maiúsculas:
print(nome.upper().strip())

# O nome com todas as letras miniúsculas:
print(nome.lower().strip())

# Quantas letras ao todo (sem considerar espaços):
print(len(nome.strip()))

# Quantas letras tem o primeiro nome
# comando passo a passo:
# div1 = nome.split()
# div2 = div1[0]
# print (len(div2))

# comando simplificado:
print(len(nome.split()[0]))
