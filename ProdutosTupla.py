listaProd = ('Café', 7.88, 'Leite', 3.50, 'Pão', 13.99, 'Presunto', 2.65)

print('-'*40)
print(f"{'LISTAGEM DE PREÇOS':>28}")
print('-'*40)

for p in listaProd:
    nomeProd, precoProd = listaProd
    print(nomeProd, precoProd)
