cont = total = 0
n = int(input('Informe um número [999 para parar]: '))
while(n != 999):
    cont += n
    total += 1
    n = int(input('Informe um número [999 para parar]: '))
print('Total de números digitados: {}'.format(total))
print("Soma dos números:  {}".format(cont))
