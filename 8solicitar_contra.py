contra = int(input("Ingrese su contaseña: "))
password = 12345678
contador = 0
while contra != password:
    contador += 1
    print("Contraseña incorrecta.")
    contra = int(input("Ingrese de nuevo su contraseña: "))
    
contador += 1
print("ACCESO CONCEDIDO. Lo has logrado en", contador, "intentos.")

        