class SerVivo:
    def __init__(self, pontos_vida, pontos_ataque):
        self.pontos_vida = pontos_vida
        self.pontos_ataque = pontos_ataque

    def __str__(self):
        return f'O ser vivo possui {self.pontos_vida} pontos de vida e {self.pontos_ataque} pontos de ataque'
    
    def atacar(self, individuo):
        individuo.pontos_vida -= self.pontos_ataque


class Personagem(SerVivo):
    def __init__(self, pontos_vida, pontos_ataque, nome):
        super().__init__(pontos_vida, pontos_ataque)
        self.nome = nome

    def __str__(self):
        return f'O personagem chama-se {self.nome}, possui {self.pontos_vida} pontos de vida e {self.pontos_ataque} pontos de ataque'


class Monstro(SerVivo):
    def __init__(self, pontos_vida, pontos_ataque, tipo):
        super().__init__(pontos_vida, pontos_ataque)
        self.tipo = tipo

    def __str__(self):
        return f'O monstro possui {self.pontos_vida} pontos de vida e {self.pontos_ataque} pontos de ataque e é do tipo {self.tipo}'

class Lobo(Monstro):
    def __init__(self, pontos_vida, pontos_ataque, tipo, forca):
        super().__init__(pontos_vida, pontos_ataque, tipo)
        self.forca = forca

    def __str__(self):
        return f'O lobo possui {self.pontos_vida} pontos de vida e {self.pontos_ataque} pontos de ataque e tem {self.forca} de força e é do tipo {self.tipo}.'
        

class Goblin(Monstro):
    def __init__(self, pontos_vida, pontos_ataque, tipo, inteligencia):
        super().__init__(pontos_vida, pontos_ataque, tipo)
        self.inteligencia = inteligencia

    def __str__(self):
        return f'O goblin possui {self.pontos_vida} pontos de vida e {self.pontos_ataque} pontos de ataque e tem {self.inteligencia} de inteligência e é do tipo {self.tipo}.'

# ATACANTE
goblin = Goblin(10, 15, 'monstro', 23) # ATAQUE=15

# ATACADOS
ser_vivo = SerVivo(60, 50) # VIDA INICIAL=60
personagem = Personagem(50, 50, "João") # VIDA INICIAL=50
monstro = Monstro(40, 50, 'ogro') # VIDA INICIAL=40
lobo = Lobo(30, 20, 'animal', 23) # VIDA INICIAL=30
outro_goblin = Goblin(20, 50, 'monstro', 23) # VIDA INICIAL=20

goblin.atacar(ser_vivo)
goblin.atacar(personagem)
goblin.atacar(monstro)
goblin.atacar(lobo)
goblin.atacar(outro_goblin)

# MOSTRANDO A QUANTIDADE DE VIDA RESTANTE DOS ATACADOS (utilizando __str__)

print(ser_vivo) # VIDA FINAL=45
print(personagem) # VIDA FINAL=35
print(monstro) # VIDA FINAL=25
print(lobo) # VIDA FINAL=15
print(outro_goblin) # VIDA FINAL=5






