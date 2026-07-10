from functools import reduce

def somar_nota(delta):
    def soma(nota):
        return nota + delta
    return soma

notas = [6.4,7.2,5.4,8.4]
notas_finais1 = list(map(somar_nota(1.5),notas))
# aplica a fincao soma_nota as notas
notas_finais2 = list(map(somar_nota(1.6),notas))
# Estou usando Anaconda e para dar certo preciso transformar em list

print(notas_finais1)
print(notas_finais2)

def soma(a, b):
    return a +b

total = reduce(soma, notas, 0)
# funcao soma passa em todas as notas
print(total)


# for i, nota in enumerate(notas):
#     notas[i]= nota[i] + 1.5

# for i in range(len(notas)):
#     notas[i]= notas[i] + 1.5


    