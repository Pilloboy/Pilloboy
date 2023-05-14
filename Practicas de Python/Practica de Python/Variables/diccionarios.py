#Creando diccionarios con dict (Horizontal)
diccionario = dict(nombre ="Leonel", apellido="Torres Rodríguez",edad= 16)

#Creando diccionario de forma vertical
diccionario = {
    "nombre": "Leonel",
    "Apellido": "Torres Rodríguez",
    "Novia": "Vanessa"
}

#Las listas no pueden ser claves porque son mutables y usamos frozenset para meter conjuntos
diccionario = {frozenset(["Nombre", "Apellido"]): "nombre"}

#Creando diccionarios con fromkeys() con dos parámetros
diccionario1 = dict.fromkeys(["Nombre", "Apellido"])

#Creando diccionarios con fromkeys() con dos parámetros cambiando el valor por defecto a "no sé"
diccionario = dict.fromkeys(["Nombre", "Apellido"], "no sé",)

print(diccionario1)