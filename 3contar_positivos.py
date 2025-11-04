numero = int(input("Ingrese un número(negativo para salir): "))
contador = 0 
while numero >= 0:
    contador = contador + 1
    numero=int(input("Ingrese otro número(negativo para salir): "))

print ("La cantidad de positivos ingresados fue de: ", contador)