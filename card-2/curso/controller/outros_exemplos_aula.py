pessoas = ['Gui', 'Rebeca']
adjs = ['Sapeca', 'Inteligente']

for p in pessoas:
    for a in adjs:
        print(f'{p} é {a}')
# printa para cada pessoa os dois adjetivos
for i in [1,2,3]:
    pass

for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i, end=' ')
# de 1 a 11 printa se nao e par
for i in range(1,11):
    if i == 5:
        break
    print(i)
    # printa os numeros se for 5 para o for

print('Fim!')