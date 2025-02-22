#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
'''
lista = []
dados = []
listagem_menor = []
listagem_maior = []
pessoas= 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    pessoas+=1
    lista.append(dados[:])
    dados.clear()
    pergunta = str(input("Quer continuar ?").strip().lower()[0])
    if pergunta in 'n':
        break
    elif pergunta in 's':
        continue
    else:
        print("Resposta inválida.", end= '')
        if str(input("Voce quer continuar ? (sim ou nao)").lower().strip()[0]) == 's':
            continue
        break
peso_menor = 0
peso_maior = 0
c = 0
for p in lista:
    if c > 0:
        if p[1] <= peso_menor:
            listagem_menor.append(p)
            peso_menor = p[1]
            continue

        elif p[1] >= peso_maior:
            listagem_maior.append(p)
            peso_maior = p[1]
            continue
    listagem_menor.append(p)
    listagem_maior.append(p)
    peso_menor = peso_maior = p[1]
    c+=1
    continue

maximo = max(listagem_maior)
minimo = min(listagem_menor)
print(f"Você cadastrou {pessoas} pessoas")
print(f"O maior peso foi {maximo[1]} de ", end= '')
for posM in listagem_maior:
    if posM[1] == peso_maior:
        print(f"{posM[0]}", end= ' ')

print(f"\nO menor peso foi {minimo[1]} de ", end= '')
for posm in listagem_menor:
    if posm[1] == peso_menor:
        print(f"{posm[0]}", end=' ')
'''

#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.
'''
lista=[[],[]]

for c in range(1,8):
    num=int(input(f"Digite o {c}o valor: "))
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 == 1:
        lista[1].append(num)
    else:
        print("Número inválido")


lista[0].sort()
lista[1].sort()

print(f"Os valores pares digitados foram: {lista[0]}")
print(f"Os valores inpares digitados foram: {lista[1]}")'''

#Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.
'''
matriz=[[0,0,0],[0,0,0],[0,0,0]]
for p in range(0,3):
    for ps in range (0,3):
        #matriz[p].append(int(input("Digite um numero para a posição ({p},{ps}): ")))
        matriz[p][ps]=int(input(f"Digite um numero para a posição ({p},{ps}): "))

for l in range(0,3):
    for c in range(0,3):
        print(f"{matriz[l][c]}", end=' ,')
    print( )'''

#Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
'''
matriz=[[],[],[]]
total_par = total_col = maior = 0
for p in range(0,3):
    for ps in range (0,3):
        num =int(input(f"Digite o número para a casa ({p},{ps}): "))
        matriz[p].append(num)
        if num % 2 == 0:
            total_par+=num
        if p == 2:
            total_col+=num
        if ps == 1 and not maior == 0:
            maior= num
        maior=num

print(f"A soma dos valores par é {total_par}")
print(f"A soma dos valores da terceira coluna é {total_col}")
print(f"E o maior valor da segunda linha é {maior}")'''

#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
matriz=[[0],[0],[0],[0],[0],[0]]
verificar = []
jogos=int(input("Quantos jogos vc quer sortear ? "))
for c in range(1,jogos+1):
    for p in range(0,6):
        valor = randint(1,60)
        matriz[p][0]= (valor)

        if valor in verificar:
            a =verificar.index(valor)
            verificar.pop(a)
            continue
        verificar.append(valor)
    matriz.sort()
    print(f"Seu {c}o jogo esta aqui: {matriz}")
    verificar.clear()