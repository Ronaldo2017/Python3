from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 5):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    tot = atual - nasc
    if tot >= 18:
        maior += 1
    elif tot < 18:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(maior))
print('E também tivemos {} pessoas menores de idade.'.format(menor))

