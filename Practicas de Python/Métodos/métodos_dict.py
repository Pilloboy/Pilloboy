diccionario = {
    "Nombre": "Leonel",
    "Novia": "Vanessa",
    "Edad": 16
}
#Devuelve un objeto dict_item 
claves = diccionario.keys()

#Obteniendo un valor con get (no me lanza una excepción y si no encuentra nada el programa continua)
valor_de_Novia = diccionario.get("Novia")

#Eliminando todo del diccionario 
#diccionario.clear()

#Eliminando un elemento del diccionario 
diccionario.pop("Nombre")

#Obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)