#Creando las listas
frutas = ["Manzana", "Pera", "Cereza", "Ciruela", "Granada", "Mora azul"]
numeros = [2,4,8,10]
cadena_de_texto = "Ti amo Vanessa"

#Evitando que se coma una fruta con continue 
for fruta in frutas:
    if fruta == "Ciruela":
        continue
    print(f"Me voyb a comer una: {fruta}")
    
#Evitar que el bucle siga ejecutandose (el else no sé ejecuta tampoco)
for fruta in frutas:
    print(f"Me voy a comer una: {fruta}")
    if fruta == "Ciruela":
        break
else:
    print("Se termino el bucle")
    
#Recorrer una cadena de texto
for letras in cadena_de_texto:
    print(letras)
    
#For en una sola línea de código (duplicamos los números por el doble)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)