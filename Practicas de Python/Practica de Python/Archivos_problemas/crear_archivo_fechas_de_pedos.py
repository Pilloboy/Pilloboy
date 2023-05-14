import pandas as pd

Fechas_de_pedos = []
 
def main():    
    Cantidad_de_pedos = [3,5,4,6,4,5,6,8,17,15,7,6,4,6,4]

    for i in range(1,16):
        Fechas_de_pedos.append(i)
    print(Fechas_de_pedos)
    with open("Archivos_problemas\\pedos.csv","a") as pedos:
        for i,n in zip(Fechas_de_pedos,Cantidad_de_pedos):
            pedos.write(f"{i},{n}\n")

if  __name__ == "__main__":
    main()
    
