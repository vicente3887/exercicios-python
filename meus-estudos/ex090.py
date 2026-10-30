"""Este programa com foco no aprendizado de dicionario, lê o nome e a média de um aluno, no final mostra a situação dele,
 se foi aprovado, reprovado ou está em recuperação"""

aluno = {}
aluno["Nome"] = str(input("Nome: "))
aluno["Media"] = float(input("Média: "))

if aluno["Media"] >= 7:
    aluno["Situacao"] = ("Aprovado")
elif aluno["Media"] <= 6 and aluno["Media"] >= 4:
    aluno["Situacao"] = ("Recuperação")
else:
    aluno["Situacao"] = ("Reprovado")

print("=-"*30)
for k, v in aluno.items():
    print(f"{k}: {v}")         