#Abriendo el archivo con with open 
with open("Archivos\\Blog_de_notas.txt", "w", encoding="UTF-8") as Archivo:
    
    #Leemos el archivo
    contenido = Archivo.writelines("Jojos es lo mejor \nNah que dices\nNo le sabes ")
    
    #Mostrando el archivo 
    print(contenido)
    
#No es necesario cerranlo al usar with open
