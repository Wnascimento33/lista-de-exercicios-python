#catetos e hipotenusa com e sem a biblioteca math
import math
c1 = float(input("digite o cateto oposto: "))
c2 = float(input("digite o cateto adjacente:"))
#hpo = (c1 ** 2 + c2 ** 2) ** (1/2)
hpo = math.hypot(c1, c2)
print(f"A hipotenuza é {hpo}")

