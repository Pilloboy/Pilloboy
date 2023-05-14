#Abriendo el archivo con with open 
with open("Archivos\\Blog_de_notas.txt", "a", encoding="UTF-8") as Archivo:
    
    #Leemos el archivo
    contenido = Archivo.write("\nTu cola no le sabe \nTu que sabras sobre ello\nno preguntes")
    
#No es necesario cerranlo al usar with open
