print('='*40)
print('10 primeiros termos de uma PA')
print('='*40)
num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = num + (10 - 1) * razao
for c in range(num, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')