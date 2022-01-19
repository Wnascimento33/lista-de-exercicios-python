from math import radians,sin,cos,tan

angulo = float(input("digite o ângulo desejado:"))
seno = sin(radians(angulo))
print(f"O seno de {angulo}° é igual a {seno:.2f}")
cosseno = cos(radians(angulo))
print(f"O cosseno de {angulo}° é igual a {cosseno:.2f}")
tangente = tan(radians(angulo))
print(f"A tangente de {angulo}° é igual a {tangente:.2f} ")
