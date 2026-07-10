nota = float(input('Informe a nota do aluno: '))
# recebe bota e transforma em float
comportado = True if input('Comportamento (y/n): ') == 'y' else False
#comportamennto receb true se input for y se nao Flase

# verifica em qual parte a nota entao, o elif é um if seguido pelo primeir if, uma sequencia de ifs para verificar o estado da nota
if nota>=9 and comportado:
    print('Duas palavras: para bens! :P')
    print('Quadro de Honra')
elif nota >= 7:
    print('Aprovado')
elif nota >= 5.5:
    print('Recuperação')
elif nota >= 3.5:
    print('Recuperação + Trabalho')
else:
    print('Reprovado')
print(nota)