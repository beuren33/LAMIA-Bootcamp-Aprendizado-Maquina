from functools import reduce

# Funcoes basicas com parametros default
def saudacao(nome='Pessoa', turma='A'):
    print(f'Ola {nome} turma {turma}')
    # se nao passar nada usa os valores default

def calcular_media(nota1, nota2, prova):
    return (nota1 + nota2 + prova) / 3
# retorna algo da funcao

if __name__ == '__main__':
    saudacao('Lucas', turma='B')
    # esse bloco so roda se executar esse arquivo direto
    # se importar de outro lugar nao executa

# *args pega os argumentos em uma tupla, pode passar quantos quiser
def somar(*nums):
    total = 0
    for n in nums:
        total += n
    return total

print(somar(10, 20, 5, 8))

# **kwargs coloca os argumentos em um dicionario
def info_aluno(**kwargs):
    status = 'aprovad' if kwargs['nota'] >= 7 else 'reprovado'
    return f'{kwargs["nome"]} foi {status}'
    # acessa igual dicionario normal pelo nome da chave

print(info_aluno(nome='Lucas', nota=8.5))

# funcoes sao objetos em python da pra passar como argumento pra outra funcao
def operar(fn, a, b):
    return fn(a, b)

def subtrair(a, b):
    return a - b

print(operar(subtrair, 10, 3))

# a funcao interna lembra os valores da externa mesmo depois de terminar
def aplicar_desconto(desconto):
    def calcular(preco):
        return preco * (1 - desconto)
    return calcular
    # retorna a funcao sem executar mas executa so quando chamar o resultado

desconto1 = aplicar_desconto(0.12)
desconto2 = aplicar_desconto(0.45)
print(desconto1(100))
print(desconto2(100))

# Lambda e usada para operacoes simples usado para uma funcao especifca
aprovado = lambda aluno: aluno['nota'] >= 7
obter_nota = lambda aluno: aluno['nota']
somar_notas = lambda a, b: a + b

alunos = [
    {'nome': 'Ana', 'nota':7.2},
    {'nome':'Breno','nota':5.1},
    {'nome':'Claudia', 'nota':8.7},
    {'nome': 'Diego','nota':6.4},
    {'nome':'Elisa', 'nota':9.0},
]
# Fiz um exemplo utilizando filter e map e depois usando comprehenshion

# filter retorna so os elementos que passam na condicao da funcao
aprovados = list(filter(aprovado, alunos))
# transformo em list por conta do Anaconda, que sem retorna o objeto

# map transforma todos os elementos usando a funcao passada
notas_aprovados = list(map(obter_nota, aprovados))

# reduce vai acumulando os elementos ate sobrar um unico valor
total = reduce(somar_notas, notas_aprovados, 0)

print(total / len(aprovados))
# media das notas dos aprovados

# List comprehension faz a mesma coisa mas de forma mais limpa
alunos_aprovados = [a for a in alunos if a['nota'] >= 7]
notas_corte = [a['nota'] for a in alunos_aprovados]
total_al = reduce(somar_notas, notas_corte, 0)

print(total_al / len(alunos_aprovados))
# mesmo resultado com comprehension uma linha no lugar de filter e map