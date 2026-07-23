total =0
qtde = 0
nota = 0

while nota != -1:
    nota = float(input('Informe o numero ou -1 para sair: '))
    if nota !=-1:
       qtde += 1
       total += nota
# enquanto nota for diferente de -1, nota recebe num de usuario, se nota for diferente de -1 qntd +1 e total +nota
print('A media da turma e: ', total/qtde)
#printa media da turma