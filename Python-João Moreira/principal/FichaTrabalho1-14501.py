
""" 1 """ 
def somar (*args):
    s = 0
    for arg in args:
        if 5 < arg < 10:
            s = s + arg
    return s

s = somar(5,6,11,23,8)
print(s)
        
""" 2 """ 
positivo_ou_negativo = lambda n: 'P' if n > 0 else 'n'
print(positivo_ou_negativo(-1))

""" 3 """ 
def inverter(num):
    inverso = 0
    while num != 0:
        inverso = inverso * 10 + num % 10
        num = num // 10
    return inverso
print(inverter(123))
""" 4 """ 
contar_digitos = lambda num: len (str(num))
numero = int(input("Digite um valor: "))
print(contar_digitos(numero))

""" 5 """ 

def perfeito(num):
    soma = 0
    for divisor in range(1,num):
        if num % divisor == 0:
            soma = soma + divisor
    if num == soma:
        print("Perfeito")
    else:
        print("Imperfeito")

perfeito(28)
perfeito(23)