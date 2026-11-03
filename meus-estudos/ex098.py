def contador(a, b, c):
    if a < b:
        for i in range(a, b, c):
            print (i)
    else:
        if c < 0:
            c = c*-1       
        for i in range(a, b, -c):
            print(i)

a = int(input("Inicio: "))
b = int(input("Fim: "))
c = int(input("Passo: "))

contador(a, b, c)