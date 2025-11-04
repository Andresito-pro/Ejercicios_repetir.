x = int(input("Ingrese un número (negativo para salir): "))
contador = 0
suma = 0

while x >= 0:
    suma += x
    contador += 1
    x = int(input("Ingrese otro número (negativo para salir): "))

if contador > 0:
    print("Su promedio es:", suma / contador)
else:
    print("No se ingresaron números válidos.")
