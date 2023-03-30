# r = 'S'
# while r == 'S':
#    sexo = input('Informe o sexo: ').strip().upper()[0]
#    if sexo != 'M':
#       if sexo != 'F':
#         sexo = input('Informe o sexo: ').strip().upper()[0]
#    r = input('Quer continuar? [S/N] ').strip().upper()[0]

sexo = input('Informe o sexo: ').strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados Inválidos. Digite novamente: ')).strip().upper()[0]
print('Sexo {} cadastrado com sucesso!'.format(sexo))
