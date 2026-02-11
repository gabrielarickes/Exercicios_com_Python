while True:
	num1 = input("Digite o primeiro número: ")
	num2 = input("Digite o segundo número: ")
	op = input("Informe a operação desejada (+-*/): ")

	numeros_validos = None

	try:
		num1_float = float(num1)
		num2_float = float(num2)
		numeros_validos = True
	except:
		numeros_validos = None
	
	if numeros_validos is None:
		print("Um ou ambos números digitados são inválidos")
		continue

	op_permitidos = '+-*/'

	if op not in op_permitidos:
		print("O operador informado é inválido")
		continue

	if len(op) > 1:
		print("Digite apenas um operador")
		continue

	if op == '+':
		print("O resultado entre {} e {} é {}".format(num1, num2, num1_float + num2_float))

	elif op == '-':
		print("O resultado entre {} e {} é {}".format(num1, num2, num1_float - num2_float))
	
	elif op == '*':
		print("O resultado entre {} e {} é {}".format(num1, num2, num1_float * num2_float))

	elif op == '/':
		if num2 == 0:
			print("Não é possível fazer divisão por 0")
			continue
		else:
			print("O resultado entre {} e {} é {}".format(num1, num2 ,num1_float / num2_float))


	sair = input("Deseja sair? [s]air: ").lower().startswith('s')

	if sair is True:
		break
