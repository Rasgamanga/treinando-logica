# Atividades pegas por Curso em Vídeo 72 a 77

'''
def main():
    lanches = ('hamburguer','suco', 'pizza', 'sorvete')
    pergunta = str(input("Quer comer algo ?")).lower().strip()[0]
    if pergunta in 's':
        comidas(lanches)
    else:
        print('ok')


def comidas (lanche):

    for comida in lanche:
        print(f"comeu {comida}")
   for comida in range(0,len(lanches)):
       print(f"Comi {lanches[comida]} na posição {comida}")
   for pos, comida in enumerate(lanches):
       print(f"Eu vou comer {comida} na posição {pos}")

if __name__ == '__main__':
    main()
'''
#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

'''
tupla = ('zero','um','dois','três','quatro','cinco','seis',
         'sete','oito','nove','dez','onze','doze','treze',
         'quatorze','quinze','dezesseis','dezessete',
         'dezoito','dezenove','vinte')


while True:
    numero = int(input("Digite um número de 0 a 20: "))
    if 0 <= numero <= 20:
        print(f"Seu número foi em extenso é {tupla[numero]}")
        if str(input("Você quer continuar ?")).lower().strip()[0] in 's':
            continue
        break
    else:
        print("Número inválido.", end=' ')
        continue
'''

#Crie uma tupla com suas 10 sobremesas preferidas. Depois mostre:
#a) Os 5 primeiros.
#b) Os últimos 4.
#c) Comidas em ordem alfabética. 
#d) Em que posição está a comida sorvete.
'''
sobremesas = ('cheesecake','torta','bolo','morango','sorvete',
              'brownie','uva','banana','chocolate','bombom')
print("Das 10 sobremesas preferidas")
print('-='*20)
print(f"As primeiras 5 sobremesas são {sobremesas[:5]}")
print('-='*20)
print(f"As ultimas 4 ultimas são {sobremesas[-4:]}")
print('-='*20)
print(f"Elas em ordem alfabetica ficarão {sorted(sobremesas)}")
print('-='*20)
print(f"Ficando em {sobremesas.index('sorvete')+1} lugar o sorvete")
'''
#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
from random import randint
num = ( randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),)
print(f"Após gerar 5 números aleatórios a tupla ficou assim : {num}")
print(f"Entre os numeros o maior é o {max(num)}")
print(f"E o menor foi {min(num)}")
'''

#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

'''
tupla = (int(input("Digite o primeiro numero: ")),
int(input("Digite o segundo numero: ")),
int(input("Digite o terceiro numero: ")),
int(input("Digite o ultimo numero: ")),)

print(f"Voce diigtou os valores {tupla}")
print(f"O valor 9 apareceu {tupla.count(9)}x")
if 3 in tupla:
    print(f"Aonde o 3 foi colocado na posição {tupla.index(3)+1}" )
print("E os números pares digitados foram: ")
for n in tupla:
    if n % 2 == 0:
        print(n)
'''

#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

'''
preços = ('borracha', 1.50,
          'Lápis', 1,
          'Caderno', 50,
          'Mochila',150)

for pos,n in enumerate(preços):
    if pos % 2 == 0:
        print(f"{preços[pos]:.<30}",end='')
    else:
        print(f"R${n:>6.2f}")
'''

#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('pao','python','framboesa','ruela','intrinsica')

for p in palavras:
    print(' ')
    print(f"Na palavra {p} tem as vogais:", end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f"{letra:}", end=' ')