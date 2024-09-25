def soma (n1, n2):
    return n1 + n2

def sub (n1, n2):
    return n1 - n2

op1 = float(input("Digite o valor 1: "))
op2 = float(input("Digite o valor 2: "))
mat = input("Digite a operação a ser executada (+ ou -): ")

if mat == "+":
    soma = op1 + op2
    print("O valor da soma é", soma)
elif mat == "-":
    sub = op1 - op2
    print("O valor da subtração é", sub)
else:
    print("Operação inválida!")