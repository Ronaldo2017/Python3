while True:
    print('-'*40)
    tabuada = int(input('Qual ver a tabuada de qual valor? '))
    print('-'*40)
    if tabuada < 0:
        print('Programa encerrado!')
        break
    for n in range(1, 11):
        print(f'{tabuada} x {n:2} = {tabuada * n:2}')
