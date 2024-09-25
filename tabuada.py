numero = int(input("Digite um número: "))

if numero > 9:
    print("Número inválido! Informe um número entre 1 e 9!")
else:
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")