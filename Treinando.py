# achei legal
'''linha = "hello world!"
for i in range(0, len(linha), 2):
  print(f'a posição {str(i)} tem a letra {linha[i]}')'''
#usando main
'''def main():
    linha = "hello world!"
    for i in range(0, len(linha), 2):
        print(f'a posição {str(i)} tem a letra {linha[i]}')
    print("Executando a função main()")

main()'''
import string

def isPalindrome(linha2):
  linha = linha2
  excluir = set(string.punctuation)

  linha = ''.join(ch for ch in linha if ch not in excluir)
  linha = linha.lower().strip().replace(' ','')
  if linha == linha[::-1]:
    print(f'{linha2} é um palindrome')
  else:
    print(f'{linha2} não é um palindrome')



# Solicitar que o usuário digite a sentença
def main():
  pergunta = ' '
  while pergunta not in 'n':
    pergunta=str(input("Quer saber se a sua palavara é um palindrome ?")).lower().strip() [0]
    if pergunta == 's':
      palavra = input('Coloque uma palavra para ver se é um palindrome: ')
      isPalindrome(palavra)
      break
    elif pergunta not in 'sn':
      print("sim ou não ?")
    else:
      print("Ok, tchau")


if __name__ == "__main__":
    main()