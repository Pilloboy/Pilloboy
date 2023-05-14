import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("c:\\Users\\TORRES RODRÍGUEZ\\Desktop\\Practicas de Python\\Practica de python\\Archivos_problemas_graficos\\dispercion.csv")

# Creando el grafico
sns.scatterplot(x="tiempo",y=" dinero",data=df)

# Mostrando el grafico
plt.show()
