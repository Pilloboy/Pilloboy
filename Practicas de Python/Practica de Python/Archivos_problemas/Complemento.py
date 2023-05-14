import pandas as pd
from crear_archivo_fechas_de_pedos import Fechas_de_pedos
    
df =pd.read_csv("Archivos_problemas\\pedos.csv", names=["FP","CP"])

df["FP"] = df.loc[:, "FP"].map(lambda value : f"01-{value}")

df.to_csv("Archivos_problemas\\archivo.csv", index=False)