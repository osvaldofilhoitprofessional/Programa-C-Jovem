def eh_par(numero):
    return numero % 2 == 0
# Chamando a função e imprimindo o  resultado

numero = int(input("Digite um número: "))
if eh_par(numero):
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
