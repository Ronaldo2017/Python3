media = maior = menor = total = cont = 0
r = 'S'
while(r == 'S'):
    num = int(input('Informe um número: '))
    cont += num  # acumula a soma dos numeros que foram digitados. ex. 5 + 5 + 5
    total += 1
    if total == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = input('Deseja continuar? S/N ').strip().upper()[0]
media = cont / total
print("Soma dos números:  {}".format(cont))
print("Total de números digitados: {} ".format(total))
print("Média: {} ".format(media))
print("Maior número: {}".format(maior))
print("Menor número: {}".format(menor))
