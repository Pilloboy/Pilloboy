import pandas as pd

def Escribir_csv(Cantidad,nombre_archivo):
    with open(f"c:\\Users\\TORRES RODRÍGUEZ\\Desktop\\Practicas de Python\\Practica de python\\Archivos_problemas_graficos\\{nombre_archivo}", "a",encoding="UTF-8") as GC:
        for i in range(Cantidad):
            Lineas = str((input(" ")))
            GC.write(f"{Lineas}\n")
            
Escribir_csv(6,"bigotes.csv")