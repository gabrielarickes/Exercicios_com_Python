frase = 'O Python é uma linguagem de programação' \
	'multiparadigma.' \
	'Python foi criado por Guido Van Rossum'

i = 0
qtd_apareceu_mais_vezes = 0
letra_que_mais_apareceu = ''

while i < len(frase):
	letra_atual = frase[i]

	if letra_atual == ' ':
		i += 1
		continue

	quantas_letras_apareceu_atual = frase.count(letra_atual)

	if qtd_apareceu_mais_vezes < quantas_letras_apareceu_atual:
		qtd_apareceu_mais_vezes = quantas_letras_apareceu_atual
		letra_que_mais_apareceu = letra_atual

	i += 1

print("A letra que apareceu mais vezes foi '{}' e quantidade foi {}x".format(letra_que_mais_apareceu, qtd_apareceu_mais_vezes))