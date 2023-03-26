from ser_vivo import SerVivo
from personagem import Personagem
from monstro import Monstro
from lobo import Lobo
from goblin import Goblin

# ATACANTE
goblin = Goblin(pontos_vida=10, pontos_ataque=15, tipo='monstro', inteligencia=23)

# ATACADOS
ser_vivo = SerVivo(pontos_vida=60, pontos_ataque=50)
personagem = Personagem(pontos_vida=50, pontos_ataque=50, nome="João")
monstro = Monstro(pontos_vida=40, pontos_ataque=50, tipo='ogro')
lobo = Lobo(pontos_vida=30, pontos_ataque=20, tipo='animal', forca=23)
outro_goblin = Goblin(pontos_vida=20, pontos_ataque=50, tipo='monstro', inteligencia=23)

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






