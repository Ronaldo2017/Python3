soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Informe {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print(soma)
print(cont)
