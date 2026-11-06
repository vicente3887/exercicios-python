
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade >= 18 and idade <= 70:
        return "Voto obrigatório"
    elif idade < 16:
        return "Voto negado"
    else:
        return "Voto opcional"

nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))