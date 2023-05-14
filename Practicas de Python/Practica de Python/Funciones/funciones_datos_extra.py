#Creando una función con dos parámetros

def frase (nombre, apellido, adjetivos):
    return f"Hola {nombre} {apellido}, eres muy {adjetivos}"

#Utilizando keyword arguments
frase_resultante = frase(nombre = "Vanessa",apellido = "Rivera Primero",adjetivo = "hermosa")
print(frase_resultante)

#Creando la misma función con un parámetro opcional y un valor por defecto 
def frase (nombre, apellido, adjetivos = "chula"):
    return f"Hola {nombre} {apellido}, eres muy {adjetivos}"

frase_resultante = frase("Vanessa", "Rivera Primero", "hermosa")
print(frase_resultante)