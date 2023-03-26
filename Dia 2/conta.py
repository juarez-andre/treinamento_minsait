from abc import abstractclassmethod

class Conta:
    def __init__(self, id_conta, saldo):
        self.id_conta = id_conta
        self.saldo = saldo

    # Métodos Abstratos
    @abstractclassmethod
    def depositar():
        pass

    @abstractclassmethod
    def sacar():
        pass

    # Getters
    @abstractclassmethod
    def get_id_conta():
        pass
    
    @abstractclassmethod
    def get_saldo():
        pass

    # Setters
    @abstractclassmethod
    def set_id_conta():
        pass
