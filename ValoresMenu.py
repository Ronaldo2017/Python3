num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))
r = 'S'
num = 0
while (r == 'S'):
    num = int(input('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa
    '''))
    print('Opção escolhida: {}'.format(num))
    if num == 1:
        s = num1 + num2
        print('A soma entre {} e {} é: {}'.format(num1, num2, s))

    if num == 2:
        m = num1 * num2
        print('A multiplicação entre {} e {} é: {}'.format(num1, num2, m))

    if num == 3:
        if num1 > num2:
            print('O maior número entre {} e {} é: {}'.format(num1, num2, num1))
        else:
            print('O maior número entre {} e {} é: {}'.format(num1, num2, num2))

    if num == 4:
        num1 = int(input('Informe um número: '))
        num2 = int(input('Informe outro número: '))

    if num == 5:
        print('Saindo do programa.....')

    r = input('Deseja continuar? [S/N] ').upper()
