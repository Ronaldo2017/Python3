frase = input('Digite a frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
if inverso == junto:
    print('É um palindromo')
else:
    print('Não é um palindromo')
