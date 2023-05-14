#2 listas, una con nombres otra con apellidos 
nombres = ["Leonel","Vanessa","Jhostin","Rigoberto","Lupita","Leticia"]
apellidos =["Torres","Rivera","Madriz","Madriz","Reyes","Rodríguez"]

#Registrar esta información en un TXT de forma óptima
with open("nombre_y_apellidos.csv","w", encoding="UTF-8") as arch:
    arch.writelines("Los datos son:\n\n")
    for i,n in zip(nombres,apellidos):
        [arch.write(f"Nombre: {i}\nApellido:{n}\n-----------\n")] 