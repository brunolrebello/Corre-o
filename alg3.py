import enum


dias_semana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado']

for indice, dia in enumerate(dias_semana):
    print(f'{indice + 1} - {dia}')

dia = int(input('Informe um número de 1 a 7: '))

print(f'O dia escolhido foi: {dias_semana[dia-1]}')


