from ser_vivo import SerVivo

class Monstro(SerVivo):
    def __init__(self, pontos_vida, pontos_ataque, tipo):
        super().__init__(pontos_vida, pontos_ataque)
        self.tipo = tipo

    def __str__(self):
        return f'O monstro possui {self.pontos_vida} pontos de vida e {self.pontos_ataque} pontos de ataque e é do tipo {self.tipo}'