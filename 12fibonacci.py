limite = int(input("Valor límite: "))
a, b = 0, 1
while a <= limite:
    print(a, end=" ")
    a, b = b, a + b
