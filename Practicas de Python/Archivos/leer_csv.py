import csv

with open("Archivos\\Datos.csv") as Archivo:
    Comentario = csv.reader(Archivo)
    for i in Comentario:
        print(i)

    
    
    
    