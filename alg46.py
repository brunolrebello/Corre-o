total=int()

for i in range(1, 6):
    numero = int(input(f'Informe o número {i}: '))
    total += numero

media = total/i
print(f'A média dos números é {media}')


