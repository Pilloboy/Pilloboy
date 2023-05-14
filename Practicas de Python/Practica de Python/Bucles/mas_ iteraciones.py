frutas = ["banana", "manzana", "pera", "sandia"]
cadena = "Hola Leonel"
numeros = 

#Evitando que se coma una manzana con continue
for fruta in frutas:
    if fruta == "sandia":
        continue
    print(f"Me voy a comer una: {fruta}")
    
#Evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f"Me voy a comer una: {fruta}")
    if fruta == "manzana":
        break
    
else:
    print("Terminado")
    
#Recorrer una cadena de texto
for letra in cadena:
    print (letra)
    
#For en una sola línea de código

