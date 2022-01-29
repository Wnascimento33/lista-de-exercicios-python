num = int(input('digite um número:'))
U = num // 1 % 10
D = num // 10 % 10
C = num // 100 % 10
M = num // 1000 % 10
print(f"A unidade é {U}.")
print(f"A dezena é {D}.")
print(f"A centena é {C}.")
print(f"A milhar é {M}.")
