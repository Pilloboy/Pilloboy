animales = set([ "gato", "loro", "cocodrilo", "pez"])
numeros = set([16,18,56,7])

#Recorriendo la conjunto animales
for animal in animales:
    print (f"ahora la variable animal es igual a: {animal}")
    
#Recoriendo la conjunto numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print (resultado)
    
#Iterando dos conjuntos del mismo tamaño al mismo tiempo
for numero, animal in zip(numeros,animales):
    print(f"Recorriendo conjunto 1: {animal} ")
    print(f"Recorriendo conjunto 2: {numero} ")
    
#Forma no optima de recorrer una lista (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
    
    
#Forma correcta de recorrer una conjunto por su indice
for num in enumerate(numeros):
    Indice = num[0]
    Valor = num[1]
    print (f"El indice es :{Indice} y el valor es: {Valor}")
    
#Usando el for/else
for numero in numeros:
    print(f"Ejecutando el último bucle, valor actual: {numero}")
    
else:
    print("El bucle termino")
    
#Todo lo anterior funciona igualmente para tuplas y conjuntos