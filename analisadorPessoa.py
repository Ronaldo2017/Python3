media = 0
soma = 0
qtdHomem = 0
qtdMulher = 0
mulherMenorVinte = 0
nomeHomem = ''
print('='*40)
print('ANALISADOR DE IDADE')
print('='*40)
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').strip().upper()

    #media das idades do grupo
    soma += idade

    #mostra qtd de homem e mulher
    if(sexo == "M"):
        qtdHomem += 1
    elif(sexo == 'F'):
        qtdMulher += 1

    #mulheres com menos de 20 anos
    if((sexo == 'F') and (idade < 20)):
        mulherMenorVinte += 1

    #homem mais velho
    if c == 1 and sexo in 'Mm':
        homemMaisVelho = idade
        nomeHomem = nome

    if sexo in 'Mm' and idade > homemMaisVelho:
        homemMaisVelho = idade
        nomeHomem = nome
media = soma / 4

print('A idade média do grupo é: {}'.format(media))
print('Quantidade de homens: {}'.format(qtdHomem))
print('Quantidade de mulheres: {}'.format(qtdMulher))
print('Quantidade de mulher com menos de 20 anos: {}'.format(mulherMenorVinte))
print('O senhor {} com a idade de {}, é o homem mais velho.'.format(nomeHomem, homemMaisVelho))
print('='*40)
