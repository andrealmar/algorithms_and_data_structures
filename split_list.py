lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
def splitter(lista, partes):
	return list(lista[parte*len(lista)/partes:(parte+1)*len(lista)/partes] for parte in range (partes))

print(splitter(lista, 5))
