def saudacao(nome = 'Pessoa', idade = 20):
    print(f"Boa Tarde {nome}!\nVc nem parece ter {idade} anos!")
# usa os dados default da funcao
# def saudacao():
#     print(f"Boa Tarde!")

def soma_e_multiplica(a,b,x):
    return a+b * x
#retorna a soma de a e b multiplicado x

if __name__ == '__main__':
    saudacao("Alice", idade = 33)
    #cria executavel no arquivo python

