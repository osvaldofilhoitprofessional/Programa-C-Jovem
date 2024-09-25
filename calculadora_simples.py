n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("Escolha a operação (+, -, *, /): ")

if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '/':
    if n2 != 0:
        print(n1 / n2)
    else:
        print("Divisão por zero não permitida!")
else:
    print("Operação inválida!")