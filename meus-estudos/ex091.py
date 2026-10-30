"""Este programa simula a rolagem de dados d20 para 4 jogadores"""

from random import randint
from time import sleep
from operator import itemgetter

RPG = {"Player1" : randint(1, 20),
       "Player2" : randint(1, 20),
       "Player3" : randint(1, 20),
       "Player4" : randint(1, 20) }

ranking = []
ranking = sorted(RPG.items(), key=itemgetter(1), reverse=True)

print("== ROLEM OS DADOS! ==")
for k, v in enumerate(ranking):
    print(f"{k+1}° {v[0]} com {v[1]} ")
