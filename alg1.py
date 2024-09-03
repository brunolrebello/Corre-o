numeros_extenso= ['um', 'dois','três']

numero = int(input('Informe um número de 1 a 3: '))

if numero <1 or numero>3:
    print('Numero inválido.')

else:
  print(f'Seu número por extenso é: {numeros_extenso[numero - 1]}')



