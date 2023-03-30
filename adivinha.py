from random import randint

tentativas = 0
n = randint(0, 10)
print('*'*27)
print(' ### ADIVINHA O NÚMERO ### ')
print('*'*27)
num = int(input('Digite um número: '))
if num == n:
    print('Você acertou')
else:
    print('Você Errou')
while(num != n):
    num = int(input('Digite um número: '))
    # num = int(input('Tente novamente: '))
    if num == n:
        print('Você acertou')
        print('Número escolhido: {}'.format(num))
        tentativas += 1
    else:
        print('Você Errou')
    tentativas += 1

print('Total de tentativas: {}'.format(tentativas))

