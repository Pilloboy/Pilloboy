#Creando un diccionario con dict()
diccionario = dict(Nombre = "Leonel", Apellido = "Torres Rodríguez", Novia ="Vanessa")

#Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["nombre","apellido"]):frozenset(["Leonel","Torres Rodríguez"])}

#Creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre", "apellido"])

#Creando diccionarios con fromkeys() cambiando el valor por defecto a "no sé"
diccionario = dict.fromkeys(["nombre", "apellido"],"no sé")

print (diccionario)
