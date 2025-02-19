#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
'''
lista = []
maximo=[]
minimo=[]
for cont in range(0,5):
    lista.append(int(input(f"Digite um valor para a posição {cont + 1}: ")))

maxi = max(lista)
mini = min(lista)
for pos,valores in enumerate(lista):
    if maxi == valores:
        maximo.append(pos+1)
    if mini == valores:
        minimo.append(pos+1)

print(f"O maior valor foi {maxi} e aparecendo nas posições", end=' ')
for pos_max in maximo:
    print(pos_max,end='...')

print(f"\nO menor valor foi {mini} e está nas posições ",end=' ')
for pos_min in minimo:
    print(pos_min,end='...')
'''
#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
lista=[13, 12]
while True:
    num = int(input("Digite um número: "))
    if num in lista:
        print(f"Este número ja está na lista")
        if str(input("Quer continuar digitando ?").strip().lower()[0]) == 's':
            continue
        break
    elif num not in lista:
        lista.append(num)
        print(f"Número adicionado!")
        if str(input("Quer continuar digitando ?").strip().lower()[0]) == 's':
            continue
        break
    else:
        print("Digite um número válido")
        continue

print(f"A lista em ordem crescente fica: {sorted(lista)}")
'''

#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
#No final, mostre a lista ordenada na tela.

'''
lista = []

for n in range(0,5):
    num = int(input("Digite um número: "))
    if n == 0:
        lista.append(num)
    else:
        for pos in range (len(lista)):
            if num < lista[pos]:
                lista.insert(pos,num)
                break
        if num > max(lista):
            lista.append(num)
            break



print((lista))
'''

#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
'''
lista = []
while True:
    num = int(input("Digite um valor: "))
    lista.append(num)
    pergunta = str(input("Quer continuar ?").lower().strip()[0])
    if  pergunta == 's':
        continue
    elif pergunta == 'n':
        break
    else:
        print("Resposta invalida")
        print('-='*15)
        if str(input("Voce quer continuar ? (sim ou não)").lower().strip()[0]):
            continue
        else:
            break

print(f"Foi digitado no total {len(lista)} números")
lista.sort(reverse=True)
print(f"A lista dos valores em ordem descrecente fica: {lista}")
if lista.index(5) == True:
    print("Tem um número 5 em sua lista")
else:
    print("O número 5 não está presente em sua lista")
'''

#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.
'''
lista = []
pares = []
impares = []
while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    pergunta = str(input("Quer continuar ?")).lower().strip()[0]
    if pergunta in 'n':
        break
    elif pergunta in 's':
        continue
    else:
        print("Resposta invalida!")
        print('-='*15)
        if str(input("Quer continuar ?(Sim ou Não) ").strip().lower()[0]) == 's':
            continue
        break

for valor in lista:
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)

print(f"Você digitou esses valores: {lista}")
print(f"Listas de pares: {pares}")
print(f"Lista de impares: {impares} ")
'''

#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

lista=[]

expressao=str(input("Digite uma expressão(com parenteses): ")).strip()
#expressao=' '.join(expressao)
#expressao = expressao.split()
for elemen in expressao:
    if elemen == '(':
        lista.append(')')
    if elemen == ')':
        lista.pop()

if len(lista)==0:
    print("Expressão valida")

else:
    print("Expressão invalida")