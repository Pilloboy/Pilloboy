#Le pedimos al usuario que nos diga una frase (o varias)
frase = input ("Dime un texto y yo te digo cuanto te tardarias en decirlo: ")

#Creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabras_totales = frase.split(" ")

#Usamos len() para ver la cantidad de elementos que hqay en la lista
cantidad_de_palabras = len(palabras_totales)

#En caso de que tarde más de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras >= 120:
    print("Tranquilo no te pedi un testamento")

#Calculamos cuanto tardaria en decir las palabras y se lo decimos
print (f"dijiste {cantidad_de_palabras} palabras, y te tardarias {cantidad_de_palabras / 2} segundos")
print(f"Dalto lo diría en {cantidad_de_palabras * 0.7} segundos")