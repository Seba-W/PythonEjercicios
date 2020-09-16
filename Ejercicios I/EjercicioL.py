def EjercicioL(lista, busqueda):
	if busqueda in lista:
		result = lista.index(busqueda)
	else:
		result = "El elemento buscado no se encuentra en la lista definida"
	return result

myArray = ["Hola", "Mundo", "Como", "Están?", "Bye"]
buscado = "Bye"
print(EjercicioL(myArray, buscado))