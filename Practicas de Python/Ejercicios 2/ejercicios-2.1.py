#Falto el profe y los alumnos van a armarla.

#Función para obtener al asistente y al profesor según la edad.
def clase (cantidad_de_compañeros):
    
    #Creando la lista con los compañeros.
    compañeros = []
    
    #Ejecutando un for para pedir información de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese el nombre de su compañero: ")
        edad = int(input("Ingrese la edad de su compañero: "))
        compañero = (nombre,edad)
        
        #Agregando la infromación a la lista
        compañeros.append(compañero)
        
    #Ordenandolos de menor a mayor según su edad
    compañeros.sort(key = lambda x : x[1] )
    
    #Compañeros [x] devuelve una tupla con (nombre,edad) y después accedemos al nombre 
    #Para definir al asistente y al profesor 
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #Retornamos una tupla
    return asistente,profesor 

#Desempaquetamos lo que nos retorna la función 
asistente,profesor = clase(5)

#Mostrando el resultado
print(f"El profesor es: {profesor} y su asistente es: {asistente}")