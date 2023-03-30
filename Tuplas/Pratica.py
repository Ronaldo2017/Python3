lanche = ('hamburguer', 'Suco', 'Pizza', 'Pudim')
#tuplas sao imutaveis
print(lanche[1:3])#comeca no elemento 1 e vai ate o 3, desconsidera o ultimo
print(lanche[2:1])
for comida in lanche:
    print(comida)

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posicao {pos}')
print('-'*30)

for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posicao {c}')
#print(sorted(lanche))#colocar em ordem

#junta tuplas
a = (2, 3, 4)
b = (5, 6, 7, 8)
c = a + b
print(c.count(4))

#dados multiplos tipos
#del = apaga a tupla