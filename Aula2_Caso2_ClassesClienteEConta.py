class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.conta = None

    def vincular_conta(self, conta):
        self.conta = conta

    def __str__(self):
        return f"Cliente: {self.nome} (CPF: {self.cpf})"


class ContaBancaria:
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo
        self.cliente = None

    def vincular_cliente(self, cliente):
        self.cliente = cliente

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

    def __str__(self):
        return f"Conta: {self.numero} (Saldo: {self.saldo})"


print('---- Exemplos de Uso ----\n')
cliente1 = Cliente("Isaac", "123.456.789-00")
conta1 = ContaBancaria("001", 1000)

cliente1.vincular_conta(conta1)
conta1.vincular_cliente(cliente1)

print(cliente1)
print(conta1)

print('\n  --  Após depositar 500 moedas  --  \n')
cliente1.conta.depositar(500)
print(conta1)

print('\n  --  Após sacar 200 moedas  --  \n')
cliente1.conta.sacar(200)
print(conta1)