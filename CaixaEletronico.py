print('='*30)
print('    BANCO DO RONALDO   ')
print('='*30)
n = int(input('Que valor você quer sacar? R$ '))
total = n
ced = 50
totalCedulas = 0
while True:
    if total >= ced:
        total -= ced
        totalCedulas += 1
    else:
        if totalCedulas > 0:
            print(f'Total de {totalCedulas} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
            totalCedulas += 1
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCedulas = 0
        if total == 0:
            break
print('='*30)
print('OBRIGADO!!! Volte Sempre. :)')
