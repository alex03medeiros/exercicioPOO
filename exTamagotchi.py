class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"{self.nome} está comendo")

    def som(self):
        print(f"{self.nome} está emitindo som")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def som(self):
        print(f"{self.nome} está miando")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def som(self):
        print(f"{self.nome} está latindo")

class Cavalo(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def som(self):
        print(f"{self.nome} está relinchando")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def som(self):
        print(f"{self.nome} está mugindo")

# Criando instâncias das classes com o nome "bolinha" e a cor "preta"
bolinha_gato = Gato("bolinha", "preta")
bolinha_cachorro = Cachorro("bolinha", "preta")
bolinha_cavalo = Cavalo("bolinha", "preta")
bolinha_vaca = Vaca("bolinha", "preta")

# Exemplo de uso
bolinha_gato.som()
bolinha_cachorro.som()
bolinha_cavalo.som()
bolinha_vaca.som()





