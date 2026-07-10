# Classes e Objetos

class Personagem:
    def __init__(self, nome, vida=100, ataque=10):
        self.nome = nome
        self.__vida = vida  # __ torna o atributo privado nao acessa direto de fora
        self.ataque = ataque

    @property
    def vida(self):
        return self.__vida
        # property permite ler o atributo privado como se fosse publico

    @vida.setter
    def vida(self, nova_vida):
        if nova_vida >= 0:
            self.__vida = nova_vida
        # setter valida antes de setar evita vida negativa

    @property
    def status(self):
        return f'{self.nome} - Vida: {self.__vida} | Ataque: {self.ataque}'
        # property sem setter = somente leitura

p1 = Personagem('Jhon Snow', 150, 35)# cria um objeto daquela classe
p2 = Personagem('Daemon Targaryen', 180, 40)# cria um objeto daquela classe

p1.vida = 120
p2.vida = -10  # validacao no setter = nao vai setar por causa da validacao no setter

print(p1.status)
print(p2.status)

# Heranca
# lasse filha herda tudo da classe pai
class Animal:
    # energia e atr privado
    def __init__(self):
        self.__energia = 100

    @property
    def energia(self):
        return self.__energia

    def mover(self):
        self.__energia -= 10
        return self.__energia

    def descansar(self):
        self.__energia += 20
        return self.__energia

class Cachorro(Animal):
    pass
    # pass usa tudo do Animal sem modificar nada

class Gato(Animal):
    def mover(self):
        return super().mover()
        # super() chama o metodo da classe pai
        # sobrescreve o metodo mas ainda usa a logica do Animal

c1 = Gato()# cria um objeto daquela classe
print(c1.mover())
print(c1.mover())
print(c1.descansar())

