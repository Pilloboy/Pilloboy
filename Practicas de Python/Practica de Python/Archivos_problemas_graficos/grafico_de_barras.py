import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("c:\\Users\\TORRES RODRÍGUEZ\\Desktop\\Practicas de Python\\Practica de python\\Archivos_problemas_graficos\\Ganancias_Coffla.csv")

# Creando el grafico
sns.barplot(x="fuente",y="ingresos",data=df)

total_ingresos = df["ingresos"].sum()

# Mostrando el total
print(f"El total de ingresos es: {total_ingresos}")

# Mostrando el grafico
plt.show()
