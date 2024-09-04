operacao = input('Informe a operação desejada: +, - ,*, /: ')
numero2 = int(input('Informe o primeiro número: '))

numero1 = int(input('informe o segundo número '))

operacoes = {
 '+':lambda x,y:x+y,
 '-':lambda x,y:x-y,
 '*':lambda x,y:x*y,
 '/':lambda x,y:x/y,
}
 
if operacao in operacoes:
     resultado = operacoes[operacao](numero1, numero2)
     print(f'numero {numero1} {operacao} {numero2}, é {resultado}')
else:
    print('Operação inválida')