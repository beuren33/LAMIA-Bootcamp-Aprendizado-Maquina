nota = float(input('Informe a nota do aluno: '))
# recebe a nota do aluno e armazena como float
comportado = True if input('Comportamento (y/n): ') == 'y' else False
# recebe o comportamento ddo aluno

if nota>=9 and comportado:
    print('Aprovado')
elif nota < 6:
    print('Recuperação')
else:
    print('Reprovado')

print(nota)

x={}
if x:
    print('Existe dados no dicionario')
else:
    print('Nao existe dados no dicionario')

# for 
for i in range(1,11):
    if i % 2 == 0:
        print(f"{i} é par")
# em um intervalo de 1 a 10 verifica se e par

nums = [1,2,3,4,5]
for n in nums:
    print(n)
# printa cada numero da lista nums

text = 'git commit -m'

for c in text:
    print(c,end=' ')
# printa cada caractere no texto com espacamento

produto = {
    'nome': 'caderno',
    'preco': 8.80,
    'quantidade': 4,
    'descricao': 'Caderno com 100 folhas'
}

for p in produto:
    print(p, '->', produto[p], end=' ')
# printa cada chave e valor do dicionario produto
for atrib, valor in produto.items():
    print(atrib, '=>', valor, end=' ')

for valor in produto.values():
    print(valor, end=' ')
# printa todos os valores do dicionario
for atrib in produto.keys():
    print(atrib, end=' ')
# printa todos as chaves do dicionario

# While
tt =0
qt = 0
nota = 0

while nota != -1:
    nota = float(input('Informe o numero ou -1 para sair: '))
    if nota !=-1:
       qt += 1
       tt += nota

print('A media da turma e: ', tt/qt)

# Outros Utilitarios
pessoas = ['ana', 'luiza']
ajetivos = ['bonita', 'romantica']

for p in pessoas:
    for a in ajetivos:
        print(f'{p} é {a}')
# para cada pessoa na lista e imprime cada adjetivo da lista