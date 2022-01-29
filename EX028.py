from random import randint
from time import  sleep
computador = randint(0, 5) #sorteia numeros inteiros
print('-=-' * 20)
print('Em que número estou pensando de 0 a 5?')
print('-=-' * 20)
jogador = int(input("em número eu pensei?"))
print("processando...")
sleep(2)
if jogador == computador:
    print(f"Parabens você ganhou !!")
else:
    print(f"ganhei pensei no numero {computador} e não {jogador}")