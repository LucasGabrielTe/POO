class ContaBancaria:
    def __init__(self, titular="", numero="", saldo=0.0):
        self.__titular = titular
        self.__numero = numero
        self.__saldo = 0.0
        self.set_saldo(saldo)

    def set_titular(self, titular):
        self.__titular = titular

    def get_titular(self):
        return self.__titular

    def set_numero(self, numero):
        self.__numero = numero

    def get_numero(self):
        return self.__numero

    def set_saldo(self, saldo):
        saldo = float(saldo)
        if saldo < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O depósito deve ser maior que zero.")
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O saque deve ser maior que zero.")
        if valor > self.__saldo:
            return False
        self.__saldo -= valor
        return True


if __name__ == "__main__":
    conta = ContaBancaria("João", "12345", 500)
    conta.depositar(200)
    conta.sacar(100)
    print(conta.get_titular(), conta.get_numero(), conta.get_saldo())
