""" p = 3 #variavel Global
def somar(y=4): # parametro substituivel
    x = 2 #variavel local
    s = x + y
    print(s)

somar(p) # Subuistitui o parametro 
somar() """

""" def somar2(v1, v2=3, v3=None):
    if v3 is None:
        return v1 + v2
s = somar2(8, 10)
q = somar2(7) """

""" def somar3(*args):
    soma = 0
    for arg in args:
        soma = soma + arg
    return soma

print(somar3(1,2,3))
print(somar3(1,2,3))
print(somar3(1,2,3))
print(somar3(1,2,3)) """

""" def total_impares(*args):
    contagem = 0
    for arg in args:
        if arg % 2 == 1: # é impar
            contagem += 1
        return contagem """
    
""" soma = lambda x,y: x + y
print (soma(3,2))
par = lambda x: "Par" if x % 2 == 0 else "Impar"
print (par(5)) """

lista = [2,3,4]
dobro = map(lambda x: x * 2, lista)
print(list(dobro))
metado_inteira = map(lambda x: x//2, lista)
print(list(metado_inteira))
quadrado = map (lambda x: x ** 2, lista)
print(tuple(quadrado))
