import os

Ferramentas = ['Alicate', 'Martelo', 'Chave de Fendas', 'Serra']

print(Ferramentas[0])
Ferramentas[2] = 'Parafusadeira'
print(Ferramentas[2])
print(Ferramentas)
print(type(Ferramentas))

# Adicionar elemento no final da lista
Ferramentas.append('Chave de Fendas')
print(Ferramentas)

#Adicionar elemento em um lugar especifico
Ferramentas.insert(1, 'Furadeira')
print(Ferramentas)

#Criação da lista
os.system('cls')
for fr in Ferramentas:
    #Encontrar elemento da lista pela primeira letra
    if fr.startswith(('C', 'P')):
        print(f'x {fr}')

for i in range(0):
    print(Ferramentas[i])

#Remover o ultimo elemento da lista
Ferramentas.pop()
print(Ferramentas)

#Remover u elemento especifico
Ferramentas.pop(1)
print(Ferramentas)

Ferramentas.remove('Serra')
print(Ferramentas)

del Ferramentas[0]
print(Ferramentas)

#Limpar toda a lista
Ferramentas.clear()
