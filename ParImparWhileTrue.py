from random import randint
computador = randint(1, 10)
venceu = soma = tentativas = 0
print('-='*20)
print('     VAMOS JOGAR PAR OU ÍMPAR    ')
print('-='*20)
while True:
    n = int(input('Digite um valor: '))
    jogo = input('Par ou Ímpar? [P/I] ').upper().strip()[0]
    print('-=' * 20)

    tentativas += 1
    soma = n + computador

    if soma % 2 == 0:
        print(f'VOCÊ JOGOU {n} E O COMPUTADOR JOGOU {computador}. TOTAL DE {soma}, DEU PAR')
    else:
        print(f'VOCÊ JOGOU {n} E O COMPUTADOR JOGOU {computador}. TOTAL DE {soma}, DEU ÍMPAR')

    if jogo == 'p'.upper().strip()[0] and soma % 2 == 0 or jogo == 'i'.upper().strip()[0] and soma % 2 == 1:
        print('PARABÉNS! VOCÊ GANHOU!!! HEHEHEHE!!! :)')
        print('VAMOS JOGAR NOVAMENTE...')
        print('-*' * 20)
    else:
        print('PERDEU')
        print('-*'*20)
        print(f'GAME OVER! Você venceu {venceu} vez(es) em {tentativas} tentativas.')
        break
    venceu += 1
