valor = 175.5
saldos = [189, 127.4, 25.9, 175.4, 1050.9, 345.6, 175.6]

for saldo in saldos:
    if saldo >= valor:
        print("Pode viajar!")
    else:
        print("Saldo insuficiente!")