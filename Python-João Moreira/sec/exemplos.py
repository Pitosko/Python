aluno = {
    'nome' : 'JoanaMarques',
    'psi' : 13.25,
    'port' : 14.50,
    'mat' : 11.33,
}

def mediafinal(**valores):
    media = 0.0
    i = 0
    for disciplina, nota in valores.items():
        if isinstance(nota,float): 
            print(f'{disciplina}: {nota} valores')
            media = media + nota
            i = 1 + 1
            media = media / i
            return media / i

m = mediafinal(**aluno)
print(m)

alunos = {
    'Marcelo' : {'nome': 'João Moreira', 'idade': 51},
    'Jesus' : {'nome': 'Jesus Christ', 'idade': 53},
    'Armando' : {'nome': 'Armando Cristo', 'idade': 19}
}

def maioridade(**als):
    for al in als:
        print(al)

maioridade (**alunos)