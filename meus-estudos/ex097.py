"""Um print especial"""

def escreva(txt):
    tamanho = len(txt)
    print("="*tamanho)
    print(txt)
    print("="*tamanho)

txt = str(input("Digite seu texto: "))

escreva(txt)