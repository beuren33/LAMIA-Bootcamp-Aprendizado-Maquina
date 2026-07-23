def soma(a, b):
    return a + b

somar = soma
#variavel que chama a funcao soma
print(somar(2, 3))
#utiliza variavel da funcao soma

def operacao_aritmetrica(fn, op1, op2):
    return fn(op1, op2)
# fn w uma outra funcao que sera inserida para relizar a operação da fn
resultado = operacao_aritmetrica(soma, 72, 93)
print(resultado)

def sub(a,b):
    return a-b

resultado = operacao_aritmetrica(sub, 72, 93)
# operacao_aritimetrica chama como parametro a funcao sub 
print(resultado)

def soma_parcial(a):
    def concluir_soma(b):
        return a + b
    return concluir_soma
# uma funcao que chama outra funcao, retornando o resultado de concluir_soma

soma_1 = soma_parcial(1)
r1 = soma_1(2)
r2 = soma_1(3)
r3 = soma_1(4)

resultado_final = soma_parcial(10)(12)
print(resultado_final,r1,r2,r3)
