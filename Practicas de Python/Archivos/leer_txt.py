#Usando open para abrir un archivo con una codificación universal (UTF-8)
Archivo = open("Archivos\\Blog_de_notas.txt", encoding="UTF-8")

# Leer el archivo completo
# Archivos = Archivo.read()

# Leer una sola linea
linea = Archivo.readline()

#Leer linea por linea 
#lineas = Archivo.readlines()

#Cerrar el archivo
Archivo.close()

print(linea)

