#aluguel de carro
D = int(input("quantos dias ficou com o carro? "))
km = float(input("quantos Km percorreu com o carro? "))
pago = (D * 60) + (km * 0.15)
print(f"Você passou {D} dias e percorreu {km:.2f}km com o carro o preço a pagar será de R${pago:.2f}")

