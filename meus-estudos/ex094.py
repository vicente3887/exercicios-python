pessoa = {}
lista = []
total = 0
while True:
    pessoa["Nome"] = str(input("Nome: "))
    while True:
        pessoa["Sexo"] = str(input("Sexo [M/F]: ")).upper()[0]
        if pessoa["Sexo"] not in "FM":
            print("ERRO! DIGITE APENAS 'F' OU 'M'")
        else:
            break
    pessoa["idade"] = int(input("Digite sua idade: "))
    total += pessoa["idade"]
    lista.append(pessoa.copy())
    pessoa.clear()
    while True:
        i = str(input("Deseja continuar? [S/N]: ")).upper()[0]
        if i not in "SN":
            print("ERRO! DIGITE APENAS 'S' OU 'N'")    
        else:
            break
    if i == "N":
        break

print("="*30)
print(lista)
print("Total de idade: ", total)
