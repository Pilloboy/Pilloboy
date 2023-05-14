#Creando una lista con list
lista = list (["Leonel","Soy PILLOBOY", 16])

#Devuelve la cantidad de elementos de la lista 
cantidad_elementos = len(lista)

#Agregando un elemento a la lista
lista.append("Rigoberto")

#Agregando un elemento a la lista en un indice especifico
lista.insert(1, "Vanessa")

#Agregando varios elementos a la lista
lista.extend(["Promotora Profile", "Tlajomulco"]) 

#Eliminando un elemento de la lista (por su indice)
lista.pop(-1)#-1 para eliminar el último, -2 para eliminar el anteúltimo y así sucesivamente  

#Removiendo un elemento de la lista por su valor
lista.remove(16)

#Eliminando todos los elementos de la lista 
#lista.clear()

#Ordenando la lista (si usamos el parámetro reverse=True lo ordena en reversa)
lista.sort()

#Invirtiendo los elementos de una lista
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index("Vanessa")

print(elemento_encontrado)