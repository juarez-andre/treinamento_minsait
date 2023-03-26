from monstro import Monstro

class Goblin(Monstro):

    def __init__(self, pontos_vida, pontos_ataque, tipo, inteligencia):
        super().__init__(pontos_vida, pontos_ataque, tipo)
        self.inteligencia = inteligencia

    def __str__(self):
        return f'O goblin possui {self.pontos_vida} pontos de vida e {self.pontos_ataque} pontos de ataque e tem {self.inteligencia} de inteligência e é do tipo {self.tipo}.'