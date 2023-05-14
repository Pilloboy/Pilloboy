#Creando una función simple
#def saludar():
    
#Ejecutando la función simple
#saludar()

#Crear una función que tenga parámetros
#nombre = input("Dime tu nombre y te saludare: ")
def saludar(nombre, sexo):
    sexo= sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reyna"
    elif (sexo == "hombre"):
        adjetivo ="makina"
    else:
        adjetivo = "raro"
    print(f"Hola {nombre} {adjetivo} como estas?")

#Crear una función que nos retorne valores
def crear_contraseña_random (num):
    chars = "abcdfghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    return contraseña,num
    
password,primer_numero = crear_contraseña_random(8) 
print (f"Tu contraseña nueva es: {password}")
print (f"El número utilizado para crearla fue: {primer_numero}")
    
    