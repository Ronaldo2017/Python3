n = soma = 0
while True:
    n = int(input('Digite um número, [999 para parar] '))
    if n == 999:
        break
    soma += n
# print('A soma {}'.format(soma))
print(f'A soma é:  {soma}')
