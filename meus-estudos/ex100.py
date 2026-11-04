from random import randint

numeros = []

def sorteio(lista):
    print("Sorteando valores pares:")
    for i in range (0, 5):
        n = randint(0, 10)
        numeros.append(n)
        print(f"{n}", end=" ")
    print("")
    
def somaPar(lista):
    soma = 0
    print("Somando valores:")
    for value in lista:
        if value % 2 ==0:
            soma += value
    print(f"{soma}")
    

sorteio(numeros)
somaPar(numeros)


