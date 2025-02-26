'''cartaz= []
filme1 = {}

for c in (0,3):
    filme1['titulo']=str(input("Nome do filme para expor: "))
    filme1['Ano']=int(input("Data de publicação: "))
    cartaz.append(filme1.copy())


for i in cartaz:
    for k,v in i.items():
        print(f" {k}  {v}")'''

#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.
'''boletim = {}
boletim["Nome"]=str(input("Qual o nome do aluno? ").strip())
while True:
    boletim["Media"]=float(input("Qual é a sua média? "))
    if 0 < boletim["Media"] <= 10:
        break
    else:
        print("nota invalida, digite novamente")
        continue

print(f"O aluno {boletim['Nome']}")
print(f"Teve de média {boletim['Media']} , Logo:")
if boletim["Media"] >= 7:
    boletim["Situação"] = "Aprovado"
    print("Aprovado")
elif 5 <= boletim["Media"] < 7:
    boletim["Situação"] = "Recuperação"
    print("Recuperação")
else:
    boletim["Situação"] = "Reprovado"
    print("Reprovado!")'''

#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
rank= {}
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6),}

for k,v in jogo.items():
    print(f"O {k} tirou no dado {v}")
rank =sorted(jogo.items(), key=lambda item: item[1], reverse=True)
print(rank)


for i,t in enumerate(rank):
    print(f"\n{i}o Lugar:O jogador{i} com o valor de: {t[1]}")

