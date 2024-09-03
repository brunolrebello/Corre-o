combustiveis = [# É uma lista de dicionário
{
    'nome':'Disel',
    'valor': 6.50
},
{
    'nome':'Gsolina',
    'valor': 6.17
},
{
    'nome':'Etanol',
    'valor': 4.45
}
]

for indice, combustivel in enumerate(combustiveis):
    print(f'{indice} - {combustivel["nome"]}') # se ficar em aspas simples ocorre erro. O problema que o VSCode do Senai está desatualizado

escolha = int(input('Informe o numero do combustivel desejado: '))    

print(f'O valor por litro é: {combustiveis[escolha]["valor"]}')









