
resultado=int()
for i in range(5): # ou pode ser dessa forma: for i in range(1, 6). o um onde é que comece, para este exemplo, e o 6 é para parar( vai ser os números 1, 2, 3, 4, 5). Não começa do zero.
    numero = int(input(f'Informe {i+1}º numero: '))
    resultado = resultado+ numero # reescrevendo de forma abreviada(resultado += numero)

print(f'A soma dos números é: {resultado}')