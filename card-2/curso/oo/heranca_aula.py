class Carro:
    def __init__(self):
        self.__velocidade =0
        # define velocidade com atr privado

    @property
    def velocidade(self):
        return self.__velocidade
    #retorna o atr velocidade

    def acelerar(self):
        self.__velocidade +=5
        return self.__velocidade
    #retorna o atr velocidade com +5
    
    def frear(self):
        self.__velocidade -=5
        return self.__velocidade
    # retorna velocidade com -5

class Uno(Carro):
    pass
# cria uma classe uno com atrs e metodos de Carro
class Ferrari(Carro):
    def acelerar(self):
        return super().acelerar()
# cria uma classe ferrari com os metodos e atrs de carro permitindo que ela acesse atrs e metodos
c1 = Ferrari()
print(c1.acelerar())
print(c1.acelerar())
print(c1.frear())
print(c1.frear())