'''
Escreva um programa que leia 𝑁 números e determine se eles formam uma
progressão aritmética
'''

while True:

	n_entradas = input("Informe a quantidade de números a ser usados: ")

	try:
		int_n_estradas = int(n_entradas)
	except ValueError:
		print("Informe valores inteiros")
		continue

	if int_n_estradas < 2:
		print("Precisa ter mais que dois números para fazer a PA")
		continue

	numeros = []

	for i in range(int_n_estradas):
		num = input("Informe os números")
		try:
			num_float = float(num)

		except ValueError:
			print("Infome somente números")
			continue

		numeros.append(num_float)

	razao = numeros[1] - numeros[0]

	pa = True

	for i in range(2, int_n_estradas):
		if numeros[i] - numeros[i - 1] != razao:
			pa = False
			break

	if pa:
		print("É uma progressão aritmética")
		print("Razão da PA {}".format(razao))
	else:
		print("Os números não formam uma progressão aritmética")

	sair = input("Para sair tecle s ou Enter para continuar ").lower()
	if sair == 's':
		break