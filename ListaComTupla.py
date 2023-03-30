time = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
	'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza',	'São Paulo', 'América-MG',
  	'Botafogo',	'Santos', 'Goiás',	'Red Bull',	'Coritiba',	'Cuiabá', 'Ceará',
	'Atlético-GO',	'Avaí','Juventude')

#tabela do campeonato brasileiro
print('-'*50)
print(f"{'Lista de times do Brasileirão':>28}")
print('-' * 50)
for t in time:
	print(t)
print('-' * 50)
#OS 5 PRIMEIROS COLOCADOS
print('OS 5 PRIMEIROS COLOCADOS')
print(time[0:5])
print('-'*50)
# 4 útlimos colocados
print('OS 4 útlimos colocados')
print(time[16:])
print('-'*50)
#ordem alfabetica
print('TIMES EM ORDEM ALFABÉTICA')
print(sorted(time))
print('-'*50)
#posicao de um time
print('Posição do Avaí')
posicao = time.index('Avaí')
print(f'O time do Avaí está na {posicao}º posição.')
print('-'*30)


