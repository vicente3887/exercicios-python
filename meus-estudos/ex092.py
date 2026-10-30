from datetime import datetime

trabalhador = {}
trabalhador["Nome"] = str(input("Nome: "))
trabalhador["Nascimento"] = int(input("Ano de Nascimento: "))
trabalhador["idade"] = datetime.now().year - trabalhador["Nascimento"]
trabalhador["Carteira"] = int(input("Carteira de Trabalho (0 para não tem): "))

if trabalhador["Carteira"] != 0:
    trabalhador["Ano de Contratacao"] = int(input("Ano de contratação: "))
    trabalhador["Salario"] = float(input("Salário: R$"))
    trabalhador["Aposentadoria"] = ((trabalhador["Ano de Contratacao"] + 35) - datetime.now().year) + trabalhador["idade"]

print("="*30)
for k, v in trabalhador.items():
    print(f"{k} = {v}")