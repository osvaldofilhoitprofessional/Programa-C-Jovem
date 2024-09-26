def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 == 0:
        return "Erro: Divisão por zero não é permitida."
    return n1 / n2

def imprimir_borda(titulo):
    borda = "*" * len(titulo)
    print(borda)
    print(titulo)
    print(borda)

def calcular():
    while True:
        print("")
        print("+", "- SOMA")
        print("-", "- SUBTRAÇÃO")
        print("/", "- DIVISÃO")
        print("*", "- MULTIPLICAÇÃO")
        print("*" * 30)

        # Recebendo os números de entrada
        try:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: Por favor, insira valores numéricos válidos.")
            continue

        # Recebendo a operação desejada
        operacao = input("Selecione a operação desejada (+, -, *, /): ")

        if operacao == "+":
            print(f"O resultado da soma é: {soma(n1, n2)}")
        elif operacao == "-":
            print(f"O resultado da subtração é: {subtracao(n1, n2)}")
        elif operacao == "*":
            print(f"O resultado da multiplicação é: {multiplicacao(n1, n2)}")
        elif operacao == "/":
            resultado_divisao = divisao(n1, n2)
            print(f"O resultado da divisão é: {resultado_divisao}")
        else:
            print("Operação inválida! Tente novamente.")
            continue

        # Perguntar se o usuário deseja continuar
        continuar = input("Deseja realizar outra operação? (s/n): ").lower()
        if continuar != 's':
            print("Encerrando a calculadora. Até mais!")
            break

# Início do programa
titulo = "A primeira calculadora"
imprimir_borda(titulo)
calcular()