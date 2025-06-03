class Conta:
    def __init__(self, numero, saldo ):
        self._numero = numero
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor
        # aqui ele acrescenta o valor ao saldo

    def sacar(self, valor):
        self._saldo -= valor

    def extrato(self):
        return self._saldo

conta = Conta(123, 1000)
conta.depositar(500)
print(conta._numero)
print(conta._saldo) #metodo errado de entra em uma privada
print(conta.extrato()) #método certo