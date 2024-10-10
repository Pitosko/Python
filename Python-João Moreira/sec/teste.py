print("Tropa Jesus Christ")
print("Atenção")


#Estrutura condicional
'''
    dsajdbvhjsadvjsadvjhsavdjhsadjhsvajdv
    sd
    sa
    dsa
    dsa
    dsa
    d
'''

x = 5
if x > 7:
    print("conseguiu")
    print("teste")
elif x < 3:
    print("chumbado")
else:
    print("tentar novamente")

# print(type(x))
x = "Marcelo"
n = 18
# print(x)
# print(type(x))

""" print("O meu nome é",x, "e a minha idade é", n)
print("O meu nome é " + x + " e a minha idade é " + str(n))
print(f'O meu nome é {x} e a minha idade é {n}') """

""" produto1 = "Martelo"
produto2 = "Alicate"
produto3 = "Tesoura"

print(produto1, end=',')
print(produto2, end=',')
print(produto3) """

import os # importa todas as funcções do modulo
from random import randrange # Importa a função randrange do modulo 

""" num1 = randrange(1,10)
print(num1)
os.system("cls")
num2 = randrange(1,20)
print(num2)
os.system("cls") """

""" num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))
print ("Soma =", num1+num2+num3) """

frase = "Maioria dos alunos"
print(frase[0:12]) #primeiros 11 caracteres
print(frase[12:]) 
print(len(frase)) #Total de caracteres na frase

frase = "maioria dos alunos"
frase2 = frase.replace("Maioria", "Minoria")
print(frase2)

lista_de_palavras = frase.split(" ")
print(type(lista_de_palavras))
print(lista_de_palavras)