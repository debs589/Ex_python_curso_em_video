"""Crie um programa que leia o nome de uma pessoa e
#diga se ela tem "SILVA" no nome"""

nome = str(input('Digite o seu nome completo: '))

"""comando strip - tirar todos os espaços à direita e à esquerda
comando upper - deixar nome em maiúsculo"""

nome1 = nome.strip().upper()

#comando find - verificar se NÃO existe "SILVA" no nome

if nome1.find('SILVA') == -1:
    print('O seu nome NÃO possui "SILVA"')
else:
    print('O seu nome possui "SILVA"')

