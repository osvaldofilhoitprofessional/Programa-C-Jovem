from time import sleep

contador = 11

print("CONTAGEM REGRESSIVA...")
while contador > 0:
    contador -= 1 #contador = contador - 1
    print(contador, '...')
    sleep(1)