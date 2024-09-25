#Calcular Média em uma lista
def calcular_media(numeros):
    total = sum(numeros)
    quantidade = len(numeros)
    return total / quantidade

# Chamando a função e imprimindo o resultado
numeros = [10, 20, 30, 40, 50]
print(f"A média dos números {numeros} é {calcular_media(numeros)}")


