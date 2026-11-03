pessoa = {}
lista = []
mulheres = []
total = 0

while True:
        pessoa.clear()
        pessoa["Nome"] = str(input("Nome: "))
        while True:
            pessoa["Sexo"] = str(input("Sexo [M/F]: ")).upper()[0]
            if pessoa["Sexo"] not in "FM":
                print("ERRO! DIGITE APENAS 'F' OU 'M'")
            else:
                break
        if pessoa["Sexo"] == "F":
            mulheres.append(pessoa["Nome"])
        pessoa["idade"] = int(input("Digite sua idade: "))
        total += pessoa["idade"]
        lista.append(pessoa.copy())
        while True:
            i = str(input("Deseja continuar? [S/N]: ")).upper()[0]
            if i not in "SN":
                print("ERRO! DIGITE APENAS 'S' OU 'N'")    
            else:
                break
        if i == "N":
            break    
print("="*30)
print(f"O total de pessoas é {len(lista)}")
media = total/len(lista)
print(f"A Média de idade é: {media:2.5f}")
print("A lista de mulheres é: ", mulheres)
print("A lista de pessoas com idade acima da média é: ")
for i in lista:
    if i["idade"] >= media:
        print("   ", end=" ")
        for k, v in i.items():
            print(f"{k} = {v}; ", end=" ")
        print( )
print("Fim do programa")