#Crie um programa que leia o nome de uma
#cidade e diga se ela começa ou não
#com o nome "SANTO".

cidade = str(input('Digite o nome da cidade: '))

#comando strip - tirar todos os espaços à direita e à esquerda
#comando upper - deixar nome em maiúsculo
#comando split - separar palavras

cidade1 = cidade.strip().upper().split()

#verificar se primeira palavra é "SANTO"

if cidade1[0] == 'SANTO':
    print('O nome da cidade começa com "SANTO"')
else:
    print ('O nome da cidade NÃO começa com "SANTO"')


