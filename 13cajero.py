saldo = 1000
while saldo > 0:
    retiro = int(input("Monto a retirar: "))
    if retiro <= saldo:
        saldo -= retiro
        print("Saldo restante:", saldo)
    else:
        print("Fondos insuficientes.")
