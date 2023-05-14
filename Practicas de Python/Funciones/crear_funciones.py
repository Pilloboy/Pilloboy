#Creando una función simple
def saludar(nombre,sexo):
    sexo = sexo.capitalize()
    if sexo == "Hombre":
        adjetivo = "titan"
    elif sexo =="Mujer":
        adjetivo = "reyna"
    else:
        adjetivo = "raro"
    print(f"Hola {nombre}, {adjetivo} qué tal estas?")

#Ejecutando la función simple    
saludar("Vanessa","muJeR")

#Crear una función que nos retorne valores
def crear_contraseña (num):
    chars = "abcdefghij"
    numero = str(num)
    num = int(numero[0])
    c1 = num -2
    c2 = num 
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    return contraseña, num

password,número = crear_contraseña(94)
frase = f"Tu contraseña es: {password} y el número utilizado fue: {número}"
print(frase)