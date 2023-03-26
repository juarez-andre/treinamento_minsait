from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, id_conta, saldo):
        super().__init__(id_conta, saldo)
        self.taxa_rendimento = 10
    
    def get_saldo(self):
        return self.saldo
    
    def get_id_conta(self):
        return self.id_conta
    
    def set_id_conta(self, novo_id):
        self.id_conta = novo_id

    def checar_rendimento(self, quantidade, unidade_tempo):
        try:
            if int != type(quantidade) != float or quantidade <= 0:
                raise ValueError("Valor Inválido.")
            
            if unidade_tempo.upper() == "SEGUNDOS":
                rendimento = (self.taxa_rendimento * quantidade * self.saldo) / 3153600000
                print(f"Em {quantidade} segundos, seu saldo atual renderá um total de R${rendimento:.2f}")
            
            elif unidade_tempo.upper() == "MINUTOS":
                rendimento = (self.taxa_rendimento * quantidade * self.saldo) / 52560000
                print(f"Em {quantidade} minutos, seu saldo atual renderá um total de R${rendimento:.2f}")

            elif unidade_tempo.upper() == "HORAS":
                rendimento = (self.taxa_rendimento * quantidade * self.saldo) / 876000
                print(f"Em {quantidade} horas, seu saldo atual renderá um total de R${rendimento:.2f}")

            elif unidade_tempo.upper() == "DIAS":
                rendimento = (self.taxa_rendimento * quantidade * self.saldo) / 36500
                print(f"Em {quantidade} dias, seu saldo atual renderá um total de R${rendimento:.2f}")

            elif unidade_tempo.upper() == "SEMANAS":
                rendimento = (self.taxa_rendimento * quantidade * self.saldo) / 5200
                print(f"Em {quantidade} semanas, seu saldo atual renderá um total de R${rendimento:.2f}")            

            elif unidade_tempo.upper() == "MESES" or unidade_tempo.upper() == "MÊSES":
                rendimento = (self.taxa_rendimento * quantidade * self.saldo) / 1200
                print(f"Em {quantidade} mêses, seu saldo atual renderá um total de R${rendimento:.2f}")

            elif unidade_tempo.upper() == "ANOS":
                rendimento = (self.taxa_rendimento * quantidade * self.saldo) / 100
                print(f"Em {quantidade} anos, seu saldo atual renderá um total de R${rendimento:.2f}")
            
            else:
                raise ValueError("Unidade de Tempo Inválida.")
        
        except ValueError as error:
            print(error)
    
    def sacar(self, valor=0):
        try:
            # Checando se o valor é um número e se é maior do que 0
            if int != type(valor) != float or valor <= 0:
                raise ValueError("Valor Inválido.")

            # Checando se o valor do saldo é maior ou igual do que valor de saque.
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque realizado com sucesso! Seu saldo atualmente é de R${self.saldo:.2f}.")
            else:
                raise ValueError("Saldo insuficiente")

        except ValueError as error:
            print(error)

    def depositar(self, valor=0):
        try:
            # Checando se o valor é um número e se é maior do que 0
            if int != type(valor) != float or valor <= 0:
                raise ValueError("Valor Inválido.")
                
            else:
                self.saldo += valor
                print(f"Depósito realizado com sucesso! O valor de saldo na sua conta agora é R${self.saldo:.2f}.")
        
        except ValueError as error:
            print(error)