import csv 

with open("Archivos\\Notas_de_cariño.csv","r",encoding="UTF-8") as Archivo:
        reader = csv.reader(Archivo)
        for row in reader:
            print(row)