print("Programa de Cálculo mediante Operaciones Matemáticas Básicas")

Num1 = int(input("Ingrese el primer Número: "))
Num2 = int(input("Ingrese el segundo Número: "))
operacion = int(input("""\nOperaciones Disponibles
1- Suma
2- Resta
3- Multiplicación
4- División
5- Todas las anteriores
Ingrese el número correspondiente a la operación: """))

if operacion <= 5 and operacion >= 1:
	print("\nUsted ha elegido la operación correspondiente al Nº" + str(operacion))

	def Suma(A, B):
		print("Sumando (" + str(A) + " + " + str(B) + ") ...")
		resultadoSuma = A + B
		print("El resultado de su Suma es " + str(resultadoSuma))

	def Resta(I, R):
		print("Restando (" + str(I) + " - " + str(R) + ") ...")
		resultadoResta = I - R
		print("El resultado de su Resta es " + str(resultadoResta))

	def Multiplicacion(X, Y):
		print("Multplicando (" + str(X) + " * " + str(Y) + ") ...")
		resultadoMultip = X * Y
		print("El resultado de su Multiplicación es " + str(resultadoMultip))

	def Division(D1, D2):
		if D2 != 0:
			print("Dividiendo (" + str(D1) + " / " + str(D2) + ") ...")
			resultadoDivi = D1 / D2
			print("El resultado de su División es " + str(resultadoDivi))
		else:
			print("No se puede dividir entre Cero (0)")

	def TodoJunto(func1, func2, func3, func4, Number1, Number2):
		return func1(Number1, Number2), func2(Number1, Number2), func3(Number1, Number2), func4(Number1, Number2)

	if operacion == 1:
		Suma(Num1, Num2)
	elif operacion == 2:
		Resta(Num1, Num2)
	elif operacion == 3:
		Multiplicacion(Num1, Num2)
	elif operacion == 4:
		Division(Num1, Num2)
	elif operacion == 5:
		TodoJunto(Suma, Resta, Multiplicacion, Division, Num1, Num2)

	print("\nEl Programa ha finalizado correctamente")

else:
	print("Haz introducido un Número Incorrecto")