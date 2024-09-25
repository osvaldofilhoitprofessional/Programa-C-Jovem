altura = float(input("Digite a altura do paciente: "))
peso = float(input("Digite o peso do paciente: "))

imc = (altura) / (peso ** 2)

if imc >= 18.5 and imc <= 24.9:
    print("Seu IMC é ", imc, " Peso normal!")
else:
    print("Seu IMC é ", imc, " Sobrepeso! Procure um nutricionista!")