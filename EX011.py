#pintando parede.

largura = float(input("digite a largura da parede: "))
altura = float(input("digite a altura da parede: "))
área = largura * altura
tinta = área / 2
print(f"A medida da parede é de {largura:.2f}x{altura:.2f} sua área é de {área:.2f}m²")
print(f"A quantidade de tinta para pintar a parede será de {tinta:.2f} litros")

