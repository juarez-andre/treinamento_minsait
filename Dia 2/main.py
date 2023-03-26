from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

print("====================================================================================================================================================")
# TESTANDO OS MÉTODOS DE CONTA POUPANÇA (AQUI A TAXA DE RENDIMENTO FOI PRÉ-DEFINIDA EM 10%)
poupanca = ContaPoupanca(id_conta=2, saldo=9347)

poupanca.depositar(20)
poupanca.sacar(250)
poupanca.sacar(170)
poupanca.checar_rendimento(365, "dias") # A checagem pode ser feita em segundos, minutos, horas, dias, semanas, mêses e anos.

print(f"Saldo: {poupanca.get_saldo()}")
poupanca.set_id_conta(4)
print(f"ID: {poupanca.get_id_conta()}")

print("====================================================================================================================================================")
# TESTANDO OS MÉTODOS DE CONTA CORRENTE
corrente = ContaCorrente(id_conta=3, saldo=50, limite=50)
# No caso de contas correntes, CASO HAJA algum prejuízo no cheque especial, o dinheiro que virá de depósitos primeiramente será usado para reestabelecer o valor do limite. Só após essa compensação que o dinheiro poderá entrar como saldo.
corrente.depositar(50)
corrente.sacar(120)
corrente.sacar(40)

print(f"Saldo: {corrente.get_saldo()}")
print(f"Cheque especial:{corrente.get_limite()}")
corrente.set_id_conta(5)
print(f"ID: {corrente.get_id_conta()}")
print(f"Saldo: {corrente.get_limite()}")
print("====================================================================================================================================================")



