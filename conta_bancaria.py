class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor 
        print('Deposito realizado com sucesso')

    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')

        else:
            self.saldo -= valor
            
    def consultar_saldo(self):
        print(f'Saldo atual: R${self.saldo:.2f}')