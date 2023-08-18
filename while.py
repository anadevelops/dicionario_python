#Repetição condicional com While
x = int(input())
while x > 0:
    x //= 2
    print (x)

#Programa para computação de valores em um caixa eletrônico
print('Iniciando nova venda...')
total = 0
while True:
    preco = int(input('Digite o preço do produto:'))
    if preco == 0:
        break
    total += preco
print("Total da venda:", total)

#Utilizando repetição condicional com alterações diferentes para cada valor
cresc_springfield = 1.01
cresc_shelbyville = 1.03
springfield = 100000
shelbyville = 30000
ano = 2017
while springfield >= shelbyville:
    springfield = springfield*cresc_springfield
    shelbyville = shelbyville*cresc_shelbyville
    ano += 1
print("Em {0}, Springfield terá {1} habitantes e Shelbyville {2}".format(ano, round(springfield), round(shelbyville)))

#Calculadora de média
soma = 0
quantidade = 0
while True:
    entrada = input("Digite um número:")
    if entrada == '':
        break
    num = float(entrada)
    soma += num
    quantidade += 1
if quantidade != 0:
    print("Média: ", soma/quantidade)
print("Nenhum número foi digitado" )