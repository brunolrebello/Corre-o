meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

for indice, mes in enumerate (meses):
    print(f'{indice+1} - {mes}')

mes_escolhido = int(input('Informe o número do mês escolhido: '))    

if mes_escolhido>2 and mes_escolhido <7:
    print ('Estamos em Outono')
elif mes_escolhido>6 and mes_escolhido <10:
    print ('Estamos em Inverno')
elif mes_escolhido>8 and mes_escolhido <13:
    print ('Estamos em Primavera')    
else:
    print('Estamos no verão')    