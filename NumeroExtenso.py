cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito',
        'nove', 'dez', 'onze', 'doze', 'treze',
        'catorze', 'quinze', 'dezesseis', 'dezesete',
        'dezoito', 'dezenove', 'vinte')
r = 'S'
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')

    r = input('Quer continuar? [S/N] ').strip().upper()[0]
print(f'Você digitou o número {cont[num]}')
