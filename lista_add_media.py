
while True:
    notas = float(input("Digite uma nota e -1 para sair do programa: "))
    for nota in notas:
        notas.append(nota)
        if nota == -1:
            break
    break

soma = 0
media = 0

for nota in notas:
    soma += nota

media = soma / len(notas)
print("A media é: ", media)



