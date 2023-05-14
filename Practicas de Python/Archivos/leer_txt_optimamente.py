#Abriendo el archivo con with open 
with open("Archivos\\Blog_de_notas.txt", encoding="UTF-8") as Archivo:
    
    #Leemos el archivo
    contenido = Archivo.read()
    
    #Mostrando el archivo 
    print(contenido)
    
#No es necesario cerranlo al usar with open
