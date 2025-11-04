num_secret = 23
intentos = 0
while True:
    ingreso = int(input("Ingrese una número entre 1 y 50: "))
    intentos += 1
    if ingreso > num_secret: 
        print ("El número es menor.")
    elif ingreso < num_secret:
        print ("El número es mayor")
    else:
        if ingreso == num_secret:
            print ("¡EL NÚMERO INGRESADO ES CORRECTO! ")
            print ("Haz acertado en ", intentos, "intentos")
            break
