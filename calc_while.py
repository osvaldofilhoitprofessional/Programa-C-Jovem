def soma(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

while True:
    op1 = float(input("Digite o valor 1: "))
    op2 = float(input("Digite o valor 2: "))
    mat = input("Digite a operação a ser executada (+, -, ou 0 para sair): ")

    if mat == "+":
        print("O valor da soma é", soma(op1, op2))
    elif mat == "-":
        print("O valor da subtração é", sub(op1, op2))
    elif mat == "0":
        break
    else:
        print("Operação inválida!")
