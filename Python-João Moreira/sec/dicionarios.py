aluno = {
    'nome': 'Joao',
    'nota_matematica': 12.5,
    'nota_portugues': 13.25,
    'outras_notas': [13,14,17,8]
}

print(aluno['outras_notas'][1])

for k in aluno: #imprime a chave
    print(k)
print('---------------------------------------')
for v in aluno.values(): #imprime values
    print(v)
print('---------------------------------------')
for k,v in aluno.items():
    print(f'{k}: {v}')
    

#chupa mos