# Variaveis
a =3
b =4.3
c = 'Test'

print(f'{a} {b} {c}')

var = float(input('Informe um numero: '))
# Pega o valor informado pelo usuario e converte para float

print(f'O numero informado ao quadrado foi {var ** 2}')

# f-strings sao feitas para facilitar a inntegração de variaveis em strings

# Basicos
print(type('ola'))
print(type(True))
print(type(2))
print(type(2.5))

# Mostra o tipo de dado da variavel

# Conjuntos
conjunto = {1,2,3,4,5,6}
print(type(conjunto))
print(conjunto)

# Dicionarios
pessoa = {
    'nome': 'Pedro Henrique',
    'idade': 20,
    'altura': 1.75,
    'peso': 70.5,
    'ativo': True
}
# criando um dicionario pessoa
print(type(pessoa))
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['altura'])
print(pessoa['peso'])
print(pessoa['ativo'])
# printa o tipo de dado da variavel e os valores do dicionario

# Listas
lista = [1,2,3,4,5,6]

lista.append(7)
# adiciona 7 a lista atraves do append
print(lista)
print(len(lista))
print(lista[3])
print(lista[-1])
# seleciona um valor pelo indice na lista

# Tuplas
tupla = (1,2,3,4,5,6)
# tupla e uma lisa imutavel que nao pode ser alterada 
print(type(tupla))
print(tupla[3])
print(tupla[-2])
print(tupla[0:3])
print(tupla[:2])
