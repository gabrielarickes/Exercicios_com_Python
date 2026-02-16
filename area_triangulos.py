'''
Implemente um programa para calcular a área de um triângulo e que não permita
a entrada de dados inválidos, ou seja, medidas menores ou iguais a 0.
'''


from math import sqrt
while True:
	print("Informe qual o tipo de triângulo que deseja descobrir a área")
	print("1: Triângulo Escaleno")
	print("2: Triângulo Isósceles")
	print("3: Triângilo Equilátero")
	print("4: Triângulo Retângulo")
	op = input("Digite a opção: " )

	try:
		int_op = int(op)

	except ValueError:
		print("Opção inválida")
		continue

	if int_op > 4 or int_op < 1:
		print("Opção inválida")
		continue

	if int_op == 1:
		while True:
			
			base = input("Informe o valor da base do triângulo: ")
			altura = input("Informe o valor da altura do triângulo: ")

			try:
				float_base = float(base)
				float_altura = float(altura)
			except ValueError:
				print("Valores inválidos")
				continue
		 
			if float_base <= 0 or float_altura <= 0:
				print("Informe valores válidos, acima de 0")
				continue

			else : 
				area = (float_base * float_altura) / 2
		
			print("O valor da área do triângulo escaleno é {}".format(area))

			break
	
	elif int_op == 2:
		while True:

			base = input("Informe o valor da base do triângulo: ")
			lado = input("Informe o valor do lado do triângulo: ")

			try:
				float_base = float(base)
				float_lado = float(lado)
			except ValueError:
				print("Valores inválidos")
				continue
		 
			if float_base <= 0 or float_lado <= 0:
				print("Informe valores válidos, acima de 0")
				continue

			else : 
				altura = sqrt( pow(float_lado,2) - pow((float_base/2), 2))

				area = (float_base * altura)	/ 2
			print("O valor da área do triângulo isósceles é {}".format(area))

			break

	elif int_op == 3:
		while True:

			lado = input("Informe o valor do lado do triângulo: ")

			try:
				float_lado = float(lado)
			except ValueError:
				print("Valores inválidos")
				continue
		 
			if float_lado <= 0:
				print("Informe valores válidos, acima de 0")
				continue

			else : 
				area = (pow(float_lado, 2) * sqrt(3) ) / 4
		
			print("O valor da área do triângulo equilátero é {}".format(area))

			break

	elif int_op == 4:
		while True:
			cateto_adj = input("Informe o valor do cateto adjacente do triângulo: ")
			cateto_oposto = input("Informe o valor do cateto oposto do triângulo: ")

			try:
				float_cateto_op = float(cateto_oposto)
				float_cateto_adj = float(cateto_adj)
			except ValueError:
				print("Valores inválidos")
				continue
		 
			if float_cateto_op <= 0 or float_cateto_adj <= 0:
				print("Informe valores válidos, acima de 0")
				continue 

			else : 
				area = (float_cateto_op * float_cateto_adj) / 2
		
			print("O valor da área do triângulo retângulo é {}".format(area))

			break

	sair = input("Para sair tecle s ou Enter para continuar ").lower()
	if sair == 's':
		break
