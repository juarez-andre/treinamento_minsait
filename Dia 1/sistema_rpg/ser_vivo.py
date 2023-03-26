class SerVivo:
    def __init__(self, pontos_vida, pontos_ataque):
        self.pontos_vida = pontos_vida
        self.pontos_ataque = pontos_ataque

    def __str__(self):
        return f'O ser vivo possui {self.pontos_vida} pontos de vida e {self.pontos_ataque} pontos de ataque'
    
    def atacar(self, individuo):
        individuo.pontos_vida -= self.pontos_ataque