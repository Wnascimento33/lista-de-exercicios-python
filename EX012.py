#porcentagem
preco = float(input("digite o preço de um produto para saber o desconto: R$"))
desc = preco * 0.05
valordesc = preco - desc
print(f"O seu produto custa R${preco:.2f}, com o desconto de R${desc:.2f}, custará R${valordesc:.2f}.")
