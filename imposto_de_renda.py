# Cálculo de Impostode Renda

renda = float(input("Digite a renda anual: "))
if renda <= 2000:
    imposto = 0
elif renda <= 5000:
    imposto = renda * 0.1
else:
    imposto = renda * 0.2

print(f"O imposto a pagar é: R${imposto:.2f}")
