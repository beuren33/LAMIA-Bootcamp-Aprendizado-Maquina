for i in range(10):
    print(i, end=' ')
#printa 10 vezes
print('')

for i in range(1, 11):
    print(i, end=' ')
#printa 1 ate 11 vezes

print('')

for i in range(1, 100,7):
    print(i, end=' ')
#vai de 1 a 99 pulando de 7 em 7
print('')

for i in range(20, 0, -3):
    print(i, end=' ')
# vai de 20 ate 0 indo de -3 em -3
print('')

nums = [2,4,6,8]

for n in nums:
    print(n, end=' ')
# printa os numeros da lista nums
print('')

texto = 'Python é muito massa!'

for letra in texto:
    print(letra, end=' ')
# printa cada caracter da string
print('')

for i in {1,2,3,4,4,4}:
    print(i, end=' ')
# printa os numeros desconsidderando as duplicadas
produto = {
    'nome': 'Caneta',
    'preco': 8.80,
    'quantidade': 0.5
}

print('')

for atrib in produto:
    print(atrib, '==>', produto[atrib], end=' ')
#printa cada chave valor do dict
print('')

for atrib, valor in produto.items():
    print(atrib, '=>', valor, end=' ')

print('')

for valor in produto.values():
    print(valor, end=' ')
print('')

for atrib in produto.keys():
    print(atrib, end=' ')
    # printa as chaves do dct