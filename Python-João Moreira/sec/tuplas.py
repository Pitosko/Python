lista = [1,2,3]
lista2 = lista        
print(lista2)
a,b,c = 1,2,3

lista = [1,2,3]
a,b,c = lista
print(a,b,c)

lista = [1,2,3]
tupla = ('a', 'b')
1 = list(tupla)
1[0] = 'c'
tupla = tuple(1)
print(tupla)