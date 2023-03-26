from ser_vivo import SerVivo

class Personagem(SerVivo):
    def __init__(self, pontos_vida, pontos_ataque, nome):
        super().__init__(pontos_vida, pontos_ataque)
        self.nome = nome

    def __str__(self):
        return f'O personagem chama-se {self.nome}, possui {self.pontos_vida} pontos de vida e {self.pontos_ataque} pontos de ataque'

