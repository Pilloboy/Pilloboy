#Cambiar el tipo de dato de una columna
import pandas as pd 
df = pd.read_csv("Archivos_problemas\\Notas_de_cariño.csv")

#Convertir a string los datos de una columna edad
df["Edad"] = df["Edad"].astype(str)
print(type(df["Edad"][0]))

#Remplazamos los datos "Leonel" por "Makina"
df["Nombre"].replace("Leonel","Vanessa",inplace=True)
print(df["Nombre"])

#Eliminando las filas con datos vacíos 
df = df.dropna()
#Eliminando las columnas con datos vacíos
df = df.dropna(axis=1)

#Eliminando las filas con datos repetidos
df = df.drop_duplicates()

#creando un csv con el dataframe resulrante (limpio)
df.to_csv("Archivos_problemas\\datos_limpios.csv")


