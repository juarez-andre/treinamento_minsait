from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, id_conta, saldo, limite):
        super().__init__(id_conta, saldo)
        self.limite_inicial = limite
        self.limite = limite

    def get_saldo(self):
        return self.saldo

    def get_limite(self):
        return self.limite
    
    def get_id_conta(self):
        return self.id_conta
            
    def set_id_conta(self, novo_id):
        self.id_conta = novo_id

    def sacar(self, valor=0):
        try:
            # Checando se o valor é um número ou se é menor ou igual do que 0
            if int != type(valor) != float or valor <= 0:
                raise ValueError("Valor Inválido.")

            # Checando se o valor de saldo somado com o valor do cheque especial satisfaz o valor do saque.
            elif self.limite + self.saldo < valor:
                raise ValueError(f"O valor do seu saldo em conta somado com o limite do cheque especial não é suficiente para atender ao saque de R${valor:.2f}.")
            
            # A partir daqui, podemos ter certeza que o saque será realizado com sucesso
            else:
                # Checando se é possível satisfazer o saque apenas com o valor de saldo em conta.
                if self.saldo >= valor:
                    self.saldo -= valor
                    print(f"Saque realizado com sucesso! Seu saldo atualmente é de R${self.saldo:.2f} e o valor do seu cheque especial é de R${self.limite:.2f}")
                
                # Aqui já é necessário fazer uso do cheque especial para realizar o saque. Tendo isso em mente, podemos assumir que o valor que restará de saldo em conta será igual a 0.
                else:
                    saldo_apos_saque = self.saldo - valor
                    self.saldo = 0
                    self.limite += saldo_apos_saque
                    print(f"Saque realizado com sucesso! Seu saldo atualmente é de R${self.saldo:.2f} e o valor do seu cheque especial é de R${self.limite:.2f}")

        except ValueError as error:
            print(error)


    def depositar(self, valor=0):
        try:
            if int != type(valor) != float or valor <= 0:
                raise ValueError("Valor Inválido.")

            # Checando se há algum prejuízo no cheque especial
            if self.limite_inicial != self.limite:
                valor_gasto_do_cheque_especial = self.limite_inicial - self.limite

                # Checando se o valor do depósito é suficiente para sanar o cheque especial
                if valor >= valor_gasto_do_cheque_especial:
                    self.limite = self.limite_inicial
                    valor -= valor_gasto_do_cheque_especial
                    # Descontados os valores pendentes do cheque especial, o resto irá entrar como saldo para a conta.:
                    self.saldo += valor
                    print(f"Depósito realizado com sucesso! O valor de saldo na sua conta agora é R${self.saldo:.2f} e o valor do seu cheque especial agora é de R${self.limite:.2f}")
                    
                # Neste caso o valor depositado não será suficiente para sanar o cheque especial, de modo que nenhum valor será acrescentado ao saldo da conta.
                else:
                    self.limite += valor
                    print(f"Depósito realizado com sucesso! O valor de saldo na sua conta agora é R${self.saldo:.2f} e o valor do seu cheque especial agora é de R${self.limite:.2f}")

            # Caso o cheque especial esteja intacto, todo o valor do depósito irá direto para o saldo
            else:
                self.saldo += valor
                print(f"Depósito realizado com sucesso! O valor de saldo na sua conta agora é R${self.saldo:.2f} e o valor do seu cheque especial agora é de R${self.limite:.2f}")

        except ValueError as error:
            print(error)