numero = int(input("Ingrese un número: "))
contador = 0
while numero > 0:
    numero = numero // 10
    contador += 1
print ("el número tiene", contador, "digitos") 