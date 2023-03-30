print('='*40)
print('10 primeiros termos de uma PA')
print('='*40)
cont = 1
num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = num
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar mais? '))
print('Finalizado com {} termos mostrados.'.format(total))
