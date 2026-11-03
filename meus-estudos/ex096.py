"""Função que calcula área"""

def área(l, c):
    area = l * c
    print(f"A área é: {area}m²")

l = float(input("Largura em metros: "))
c = float(input("Comprimento em metros: "))

área(l, c)