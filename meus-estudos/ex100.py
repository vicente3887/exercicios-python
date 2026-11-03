from random import randint

numeros = []

def sorteio():
    for numeros in range (0, 5):
        n = randint(0, 10)
        numeros.append(n)

print(sorteio)