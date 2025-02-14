'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

total = miltotal = menor = cont =0
barato = ' '
continuar=' '

while continuar not in 'n':
    produto=str(input('Qual produto vc irá comprar ?')).lower()
    preco=int(input('Qual foi o preço?'))
    total +=preco
    cont+=1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

            
    if preco > 1000: miltotal+=1

    continuar=str(input('Quer continuar ?')).lower().strip()[0]
    if continuar == 's':
        continue
    else:
        print('digite sim ou não')

print(f'o total dos produtos ficou R${total}')
print(f'O total de itens que custam mais de R$1000 foi {miltotal}')
print(f'Produto mais barato foi {barato} que custou {menor} reais')
