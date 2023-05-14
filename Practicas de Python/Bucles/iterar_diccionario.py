#Creando diccionario en vertical
diccionario = {
    "Nombre" : "Leonel",
    "Apellidos" : "Torres Rodríguez",
    "Novia" : "Vanessa"
}

#Creando un diccionario con dict()
diccionario = dict(nombre = "Leonel", apellido = "Torres Rodríguez", novia = "Vanessa")

#Recorriendo diccionarios para obtener las claves
for key in diccionario:
    print(key)
    
#Recorriendo diccionario con items() para obtener las claves y los valores
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es: {key}, y el valor es: {value}")
    
#Recorriendo un diccionario con items() nos pasa una tupla con el la clave y su valor 
for datos in diccionario.items():
    print(datos)