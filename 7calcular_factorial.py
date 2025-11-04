numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    factorial = 1
    contador = 1

    while contador <= numero:
        factorial *= contador
        contador += 1

    print("El factorial de", numero, "es:", factorial)
