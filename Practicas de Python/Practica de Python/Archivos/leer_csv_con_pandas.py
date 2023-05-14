import pandas as pd

#Usando la función read_csv para leer el archivo CSV
df = pd.read_csv("Archivos\\Notas_de_cariño.csv",names=["Name","Lastname","Age"]) 
df2 = pd.read_csv("Archivos\\Notas_de_cariño.csv",names=["Name","Lastname","Age"])

#Obteniendo los datos de la columna Nombre
nombres = df["Name"]

cadena = "0123456789"
print(cadena[-5:-1]) 

df_orden_ascendente = df.sort_values("Age")

#Ordenandolo de forma descendente
df_orden_descendente = df.sort_values("Age",ascending=False)

#Concatenando dos dataframes
df_concatenado = pd.concat([df,df2])

#Accediendo a la primer fila con head()
primer_fila = df.head(0)

#Accediendo a las últimas 3 filas de los dos dataframes con tail()
ultima_fila = df.tail(3),df2.tail(3)

#Accediendo a la cantidad de columnas y filas con shape()
filas_y_columnas_totales = df.shape

#Sacar cantidad de filas y columnas con el indice indicado
filas_totales = filas_y_columnas_totales[0]
columnas_totales = filas_y_columnas_totales[1]

#Desempaquetando la cantidad de filas y columnas
cantidad_de_filas1,cantidad_de_columnas1 = df.shape

#Obteniendo data estadistica del dataframe
df_info = df.describe()

#Accediendo a un elemento específico de df con loc
df_específico = df.loc[2,"Lastname"],df.loc[2,"Name"]

#Accediendo a un elemento específico de df con iloc
df_específico2 = df.iloc[2,1],df.iloc[2,0]

#Accediendo a todas las columnas de una fila con loc
Datos_jhostin = df.loc[2,:]
#Accediendo a todas las columnas de una fila con loc
Datos_jhostin1 = df.loc[2:2]

#Accediendo a todas las filas de una columna con iloc
Apellidos = df.iloc[:,1]
#Accediendo a todas las columnas de una fila con iloc
Datos_jhostin2 = df.iloc[2,:]

#Accediendo a filas con la edad mayor a 30
#edades_mayores_a_30 = df.loc[df["Age"],:]
#print(edades_mayores_a_30)
#print(f"Cantidad de filas: {filas_totales} y la cantidad de columnas es: {columnas_totales}")

#print(df)
