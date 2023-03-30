totalProd = gastoProd = prodMenor = prodMaior = 0
nomeProdMenor = ''
r = 'S'
print('-' * 30)
print('      LOJA SUPER BARATÃO   ')
print('-' * 30)
while True:
    nome = input('Digite o produto: ')
    preco = float(input('Digite o preço do produto: R$ '))
    totalProd += 1
    gastoProd += preco
    if preco > 1000:
        prodMaior += 1

    if totalProd == 1 or preco < prodMenor:
        prodMenor = preco
        nomeProdMenor = nome

    r = input('Quer continuar? [S/N] ').strip().upper()[0]
    if r == 'N'.strip().upper()[0]:
        print('------------ FIM DO PROGRAMA ----------')
        break

print(f'Quantidade de produto: {totalProd}')
print(f'Total da compra: R$ {gastoProd:.2f}')
print(f'Temos {prodMaior} produto(s) custando mais que R$ 1000.00')
print(f'O produto mais barato foi {nomeProdMenor} que custa R$ {prodMenor:2f}')




