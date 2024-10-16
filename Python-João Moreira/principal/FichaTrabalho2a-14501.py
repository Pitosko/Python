dados = [
    { 'nome': 'Marcelo', 'sexo': 'M', 'altura': 1.84, 'peso': 98 },
    { 'nome': 'Rui', 'sexo': 'M', 'altura': 1.94, 'peso': 83 },
    { 'nome': 'Joana', 'sexo': 'F', 'altura': 1.68, 'peso': 68 },
    { 'nome': 'Leonor', 'sexo': 'F', 'altura': 1.64, 'peso': 59 },
    { 'nome': 'Alfredo', 'sexo': 'M', 'altura': 1.87, 'peso': 105 }
]

#Devolva uma lista de 0's e 1's conforme o sexo seja M (1) ou F (0)
lista1 = map(lambda sx: 0 if sx['sexo'] == "F" else 1, dados)
print(list(lista1))

lista2 = map(lambda ps: (ps['nome'],0) if ps['sexo'] == "F" else (ps['nome'],1), dados)
print(list(lista2))

lista3 = map(lambda ps: (ps['nome'],0) if ps['sexo'] == "F" else (ps['nome'],1), dados)
print(list(lista3))

def medias(pessoas):
    media_peso = 0
    media_altura = 0

    for pessoa in pessoas:
        media_peso = media_peso + pessoa['peso']
        media_altura = media_altura + pessoa['altura']
    media_peso /= len(pessoas)
    media_altura /= len(pessoas)
    return (media_peso,round(media_altura,2))

print(medias(dados))

dados2 = {
    'a' : { 'nome': 'Marcelo', 'sexo': 'M', 'altura': 1.84, 'peso': 98 },
    'b' : { 'nome': 'Rui', 'sexo': 'M', 'altura': 1.94, 'peso': 83 },
    'c' : { 'nome': 'Joana', 'sexo': 'F', 'altura': 1.68, 'peso': 68 },
    'd' : { 'nome': 'Leonor', 'sexo': 'F', 'altura': 1.64, 'peso': 59 },
    'e' : { 'nome': 'Alfredo', 'sexo': 'M', 'altura': 1.87, 'peso': 105 }
}

def medias2(**pessoas):
    media_peso = 0
    media_altura = 0

    for pessoa in pessoas.values():
        media_peso = media_peso + pessoa['peso']
        media_altura = media_altura + pessoa['altura']
    media_peso /= len(pessoas)
    media_altura /= len(pessoas)
    return (media_peso,round(media_altura,2))

print(medias2(**dados2))