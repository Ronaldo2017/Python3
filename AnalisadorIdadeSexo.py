r = 'S'
totalMaior = 0
homemCad = 0
mulherCad = 0
while True:
    print('-='*20)
    print('          CADASTRE UMA PESSOA  ')
    print('-=' * 20)

    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').strip().upper()[0]

    if sexo not in 'M'.strip().upper()[0]:
        if sexo not in 'F'.strip().upper()[0]:
            sexo = input('Sexo: [M/F] ').strip().upper()[0]
    print('-=' * 20)

    if idade > 18:
        totalMaior += 1
    if sexo == 'm'.strip().upper()[0]:
        homemCad += 1
    if idade < 20 and sexo == 'f'.strip().upper()[0]:
        mulherCad += 1

    r = input('Quer continuar? [S/N] ').strip().upper()[0]
    if r == 'N'.strip().upper()[0]:
        print('===== FIM DO PROGRAMA =====')
        break

print(f'Maior que 18 anos: {totalMaior}')
print(f'Total homens: {homemCad}')
print(f'Total mulheres menor de 20 anos: {mulherCad}')
