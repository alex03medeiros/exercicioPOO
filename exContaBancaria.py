class ContaBancaria:

    def __init__(self, numero, saldo, nome, tipo, limite, status=False):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.limite = limite
        self.status = status

    def verificarsaldo(self):
        print(f"Saldo: R$ {self.saldo}")

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito
        print(f'Depositado um valor de: R$ {valor_deposito}')
        self.verificarsaldo()

    def sacar(self, valor_saque):
        if valor_saque > self.limite:
            print(f"O valor do saque de R$ {valor_saque} é maior que seu limite de R$ {self.limite}")
        elif valor_saque > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor_saque
            print(f'Sacado um valor de: R$ {valor_saque}')
            self.verificarsaldo()

    def ativarconta(self):
        if self.status == False:
            self.status = True
            print("Conta ativada")
        else:
            print("Essa conta já está ativada")

# Criando uma instância da classe ContaBancaria
minha_conta = ContaBancaria(numero=12345, saldo=1000.00, nome="João Silva", tipo="Conta Corrente", limite=500.00)

# Ativando a conta
minha_conta.ativarconta()

# Verificando o saldo da conta (após ativação)
minha_conta.verificarsaldo()

# Realizando um depósito
minha_conta.depositar(500.00)

# Realizando um saque
minha_conta.sacar(300.00)