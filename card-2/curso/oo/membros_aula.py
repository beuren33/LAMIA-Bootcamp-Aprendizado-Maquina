class Contador:
    contador = 0

    def inc_maluco(self):
        self.contador +=1
        return self.contador
    # modifica a variavel contador na funcao e nao na variavel global
    @classmethod
    def inc(cls):
        cls.contador +=1
        return cls.contador
    #incrementa 1 a variavel global    

    @classmethod
    def dec(cls):
        cls.contador -=1
        return cls.contador
    #decrementa 1 a variavel globa´l

    @staticmethod
    def mais_um(n):
        return n +1
    # e uma funcao da classe mas nao interfere nas variaveis

c1 =Contador()
print(c1.inc_maluco())
print(c1.inc_maluco())
print(c1.inc_maluco())
print(c1.inc_maluco())

# print(Contador.inc())
# print(Contador.inc())
# print(Contador.inc())
# print(Contador.dec())
# print(Contador.dec())
# print(Contador.dec())
# print(Contador.mais_um(99))