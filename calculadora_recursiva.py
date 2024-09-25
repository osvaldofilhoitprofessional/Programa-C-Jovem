def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    return n1 / n2

titulo = "A primeira calculadora"
borda = "*" * len(titulo)
print(borda)
print(titulo)
print(borda)

operacao = ""

while operacao not in ["+", "-", "*", "/"]:
    print("")
    print("+", "- SOMA")
    print("-", "- SUBTRAÇÃO")
    print("/", "- DIVISÃO")
    print("*", "- MULTIPLICAÇÃO")
    print(borda)

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    operacao = input("Selecione a operação desejada (+, -, *, /): ")

    if operacao == "+":
        print("O resultado da soma é:", soma(n1, n2))
    elif operacao == "-":
        print("O resultado da subtração é:", subtracao(n1, n2))
    elif operacao == "*":
        print("O resultado da multiplicação é:", multiplicacao(n1, n2))
    elif operacao == "/":
        print("O resultado da divisão é:", divisao(n1, n2))
    else:
        print("Operação inválida!")
