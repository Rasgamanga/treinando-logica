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


lista = []

for n in range(0,5):
    num = int(input("Digite um número: "))
    if n == 0:
        lista.append(num)
    else:
        for c in range (len(lista)):
            if num < lista[c]:
                lista.insert(c,num)
                break
        if num > max(lista):
            lista.append(num)
            break



print((lista))
