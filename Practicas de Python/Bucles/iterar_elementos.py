animales = ["Gato", "Perro", "Cocodrilo","Loro","Capibara","Iguana"]
numeros = [46,87,835,529,352,85]

#Recorriendo la lista animales
for animal in animales:
    print(animal)

#Recorriendo la lista numeros y multiplicando por 10
for num in numeros:
    print(num * 10)
    
#Iterando dos listas del mismo tamaño al mismo tiempo
for num,animal in zip(numeros,animales):
    print(f"La lista 1 contiene: {num}")    
    print(f"La lista 2 contiene: {animal}")    
    
#Forma no optima de recorrer una lista con su indice (no funciona con conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
    
#Forma correcta de recorrer una lista con su indice
#(enumerate() sin seleccionar por separado el indice y el valor te devuelve una tupla con dichos datos)
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice}, y su valor es: {valor}")

#Forma de desempaquetar la tupla directamente en el  for 
for numero,i in enumerate(numeros):
    print(numero,i) 
    
#Usando el for else
for num in numeros:
    print(num * 10)
else:
    print("El bucle termino")
    
#Todo lo anterior funciona exactamente igual para tuplas y conjuntos