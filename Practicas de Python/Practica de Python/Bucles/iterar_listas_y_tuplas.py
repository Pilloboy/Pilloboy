animales = list([ "gato", "loro", "cocodrilo", "pez"])
numeros = list([16,18,56,7])

#Recorriendo la lista animales
for animal in animales:
    print (f"ahora la variable animal es igual a: {animal}")
    
#Recoriendo la lista numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print (resultado)
    
#Iterando dos listas del mismo tamaño al mismo tiempo
for numero, animal in zip(numeros,animales):
    print(f"Recorriendo lista 1: {animal} ")
    print(f"Recorriendo lista 2: {numero} ")
    
#Forma no optima de recorrer una lista
for num in range(len(numeros)):
    print(numeros[num])
    
#Forma correcta de recorrer una lista por su indice
for num in enumerate(numeros):
    Indice = num[0]
    Valor = num[1]
    print (f"El indice es :{Indice} y el valor es: {Valor}")
    
#Usando el for/else
for numero in numeros:
    print(f"Ejecutando el último bucle, valor actual: {numero}")
    
else:
    print("El bucle termino")
    
#Todo lo anterior funciona igualmente para tuplas

