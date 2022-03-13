"""Escreve um programa que faça o computador "pensar" em um número
de o a 5 e peça para o usuário tentar descobrir qual foi o
número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu"""


from random import randrange
numero = randrange(6)

palpite = int(input('Advinhe qual número entre 0 e 5 que o computador escolheu: '))

if palpite == numero:
    print('Parabéns! Você advinhou o número que o computador escolheu')
else:
    print ('Poxa, não foi dessa vez! Você NÃO advinhou o número escolhido pelo computador'"\n"
           'Número escolhido pelo computador: {}'.format(numero))
