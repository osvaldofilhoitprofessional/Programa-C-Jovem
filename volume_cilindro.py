import math
from math import pi

altura = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o raio do cilindro: "))

volume = (math.pi*(raio ** 2)*altura)

print("O volume é %.2f" % volume, "em metros cúbicos.")
print("O volume é ", round(volume, 2) , "em metros cúbicos.")