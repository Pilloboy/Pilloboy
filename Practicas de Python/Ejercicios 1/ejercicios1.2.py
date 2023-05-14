#Le pedimos al usuario que nos diga una frase
frase = input("Decime una frase y te digo cuanto te tardarias en decirlo: ")

#Creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio)
palabras_totales = frase.split(" ")

#Usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(palabras_totales)

#En caso de que tarde más de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras >= 120:
    print("Hey tranquilo, no te pedi un testamento")
    
#Calculamos cuanto tardaria en decir las palabras y se lo decimos 
print(f"Dijiste {cantidad_de_palabras} palabras, y te tardarias {cantidad_de_palabras / 2} segundos")
print(f"Dalto lo diria en {cantidad_de_palabras / 2 * 0.7} segundos")    