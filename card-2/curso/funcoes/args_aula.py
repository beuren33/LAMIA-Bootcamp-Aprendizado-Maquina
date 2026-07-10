def soma(*nums):
    total = 0
    for n in nums:
        total += n
    return total
# funcao que pode receber quantos argumentos quiser
def resultado_final(**kwargs):
    status = "Aprovado(a)" if kwargs["nome"] else "Reprovado(a)"
    return f"{kwargs['nome']} foi {status}"
# premite uma funcao receber variaveis nomeadas, ex: nome = 'jhon snow'