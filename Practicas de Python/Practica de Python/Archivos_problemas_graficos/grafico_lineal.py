import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("c:\\Users\\TORRES RODRÍGUEZ\\Desktop\\Practicas de Python\\Practica de python\\Archivos_problemas\\archivo.csv")

# Creando el grafico
sns.lineplot(x="FP", y="CP", data=df)

# Creando un punto en el momento de más pedos
plt.plot("01-9", 17, "o")

# Mostrando el grafico
plt.show()
