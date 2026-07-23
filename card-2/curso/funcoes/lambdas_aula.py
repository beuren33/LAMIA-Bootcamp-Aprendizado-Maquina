from functools import reduce

alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7},
]

aluno_aprovado = lambda aluno: aluno['nota'] >=7
# se aluno tiver nota maior ou igula 7 vai em luno aprovado
# aluno_honra = lambda aluno: aluno['nota'] >=9
obter_nota = lambda aluno: aluno['nota']
# pega todas as notas de alunos
somar = lambda a,b: a+b
# soma a +b

alunos_aprovados = list(filter(aluno_aprovado, alunos))
# coloca em alunos_aprovados somente os alunos aprovados
notas_alunos_aprovados = list(map(obter_nota,alunos_aprovados))
# aplica obter nota em cada item em alunos_aprovados
total=reduce(somar,notas_alunos_aprovados, 0)
# alica a funcao somar a todos as notas alunos aprovados
print(total/ len(alunos_aprovados))

# print(obter_nota(alunos[2]))
# print(alunos)
# print(alunos_aprovados)
