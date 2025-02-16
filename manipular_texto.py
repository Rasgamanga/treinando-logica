#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.
#CURSO EM VIDEO
'''
nome = str(input("Qual é o seu nome ?"))
print(f'Seu nome todo maiusculo é {nome.upper()}')
print(f'Seu nome todo minusculo fica {nome.lower()}')
print(f"Seu nome tem {len(nome) - nome.count(' ')} letras")
print(f"Tendo {nome.find(' ')} letras em seu primeiro nome")
'''


#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

'''cidade = str(input('Qual o nome da cidade ?')).title().strip().split()
if 'Santo' in cidade[0]:
    print('Sua cidade começa com a palavra "Santo"')
else:
    print('Não começa com a palavra "Santo"')
'''


#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''
nome = str(input('Qual é o seu nome ?')).strip().title()
if "Silva" in nome:
    print('Seu Nome tem "Silva"')
else:
    print('Não tem "Silva"')
'''

#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''
nome = str(input('Digite uma frase: ')).strip().lower()
nome =''.join(nome.split())
nome = nome.replace('á','a')
print(f"Sua frase tem {nome.count('a')} letras A")
print(f"Sendo a primeira na posição {nome.find('a')+1}")
print(f"E a ultima na {nome.rfind('a')+1}")
'''

#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Qual é o seu nome completo ?")).title().strip().split()

print(f"Seu primeiro nome é {nome[0]}")
print(f"E o seu ultimo nome é {nome[-1]}")