idade = int(input("Digite a idade do cliente: "))

if idade < 5:
    print("Entrada gratuita!")
elif idade <= 12:
    print("O ingresso custa 10 reais!")
elif idade <= 18:
    print("O ingresso custa 15 reais!")
elif idade <= 60:
    print("O ingresso custa 20 reais!")
else:
    print("O ingresso custa 12 reais!")