class Acoes:
    def __init__(self, nome):
        self.nome = nome
        self.comendo = False
        self.falando = False
        self.dormindo = False
        self.parando = True

    def comer(self):
        if self.falando:
            print(f"{self.nome} não pode comer pois está falando")
        elif self.dormindo:
            print(f"{self.nome} não pode comer pois está dormindo")
        elif self.comendo:
            print(f"{self.nome} já está comendo")
        else:
            print(f"{self.nome} começou a comer")
            self.comendo = True
            self.parando = False

    def falar(self):
        if self.comendo:
            print(f"{self.nome} não pode falar pois está comendo")
        elif self.dormindo:
            print(f"{self.nome} não pode falar pois está dormindo")
        elif self.falando:
            print(f"{self.nome} já está falando")
        else:
            print(f"{self.nome} começou a falar")
            self.falando = True
            self.parando = False

    def dormir(self):
        if self.comendo:
            print(f"{self.nome} não pode dormir pois está comendo")
        elif self.falando:
            print(f"{self.nome} não pode dormir pois está falando")
        elif self.dormindo:
            print(f"{self.nome} já está dormindo")
        else:
            print(f"{self.nome} foi dormir")
            self.dormindo = True
            self.parando = False

    def parar(self):
        if self.comendo:
            print(f"{self.nome} parou de comer")
            self.comendo = False
            self.parando = True
        elif self.falando:
            print(f"{self.nome} parou de falar")
            self.falando = False
            self.parando = True
        elif self.dormindo:
            print(f"{self.nome} acordou")
            self.dormindo = False
            self.parando = True
        elif self.parando:
            print(f"{self.nome} já está parado")

# Exemplo de uso da classe Acoes
pessoa = Acoes("João")

pessoa.comer()
pessoa.falar()
pessoa.dormir()
pessoa.parar()
pessoa.comer()

print(f"{pessoa.nome} está comendo: {pessoa.comendo}")
print(f"{pessoa.nome} está falando: {pessoa.falando}")
print(f"{pessoa.nome} está dormindo: {pessoa.dormindo}")
print(f"{pessoa.nome} está parado: {pessoa.parando}")