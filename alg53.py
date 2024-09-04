from os import system
import time
numero = int(input('Infomre o número: '))

while numero >= 1:
    system('clear')
    print(numero)
    numero -=1
    time.sleep(1)
print('KABUMMM!!')