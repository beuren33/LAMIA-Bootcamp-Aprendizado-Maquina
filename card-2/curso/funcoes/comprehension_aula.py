from functools import reduce

alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7},
]

somar = lambda a,b: a+b
# laambda e uma funcao anonima, curta e especifica que pode ser resumida em uma linha, retorna a+b
alunos_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7]
# para cada aluno em alunos, coloca aluno em alunos_aprovados se a nota for maior ou igual a 7
notas_alunos_aprovados = [aluno['nota']for aluno in alunos_aprovados]
# cada nota de aluno em alunos aprovados 
total=reduce(somar,notas_alunos_aprovados, 0)
# o reduce itera sobre cada nota a funcao soma, comecando em 0

print(total/ len(alunos_aprovados))


