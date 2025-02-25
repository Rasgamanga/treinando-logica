'''lista = ['pao', 'maça', 'banana','pao', 'maça', 'banana']
lista.append('uva')
lista.remove('pao')
lista.pop()
#print(lista.index('banana',4))
#print(lista.count('maça'))
#print((str(len(lista))))
print(lista)'''

'''
lista = [-4, -2, -1, 0, 2, 4]
nova_lista = [x for x in lista if x >= 0]

print(nova_lista)'''

'''
lista = [1,7,3,6,2]
conjunto = set(lista)

print(conjunto)

lista = list(conjunto)

lista.append(1)

print(lista)
'''

'''
dict2 = {'a': 5, 'b': 10, 'c': 100, 'd': 9.5}

dict2 ['a'] = 50

dict2 ['z'] = 1000

print(dict2.keys())

'''
'''
lista = ('borracha', 2,
         'Lapís', 1.50,
         'Caderno', 50,
         'Mochila', 100)

for posicao in range (0 , len(lista)):
    if posicao % 2 == 0:
        print(f'{lista[posicao]:.<30}', end="" )
    else:
        print(f'{lista[posicao]:.2f}')'''

frase = ('pao de queijo')

#for posi in range (len(frase)):
    #if posi in 'aeiou':
frase = frase.split()
vogais = frase.count('aeiou')
print(vogais)