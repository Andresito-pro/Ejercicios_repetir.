palabra = input("Ingrese palabra: ").lower()
vocal = input("Vocal a contar: ").lower()
i = 0
cont = 0
while i < len(palabra):
    if palabra[i] == vocal:
        cont += 1
    i += 1
print("Aparece", cont, "veces.")
