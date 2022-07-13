import random

def dadosrandom(random):
    
# ¿Quién comienza?
inicio = random.randint(0, 1)
if inicio == 0:
    print('inicio el jugador')
else:
    print('inicio el PC')
# Número aleatorio del parchís
numero = random.randint(1, 6)

#def jugador(jugador):

dadosrandom()
