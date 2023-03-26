from monstro import Monstro

class Lobo(Monstro):
    def __init__(self, pontos_vida, pontos_ataque, tipo, forca):
        super().__init__(pontos_vida, pontos_ataque, tipo)
        self.forca = forca

    def __str__(self):
        return f'O lobo possui {self.pontos_vida} pontos de vida e {self.pontos_ataque} pontos de ataque e tem {self.forca} de força e é do tipo {self.tipo}.'