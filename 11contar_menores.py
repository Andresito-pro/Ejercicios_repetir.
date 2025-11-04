cont = 0
while True:
    num = int(input("Ingrese número (0 para salir): "))
    if num == 0:
        break
    if num < 50:
        cont += 1
print("Menores a 50:", cont)
