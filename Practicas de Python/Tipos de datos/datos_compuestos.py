#creando una lista (se pueden modificar sus elementos y separamos con coma cada elemento)
lista=["Leonel Torres Rodríguez", "Soy Leo", True, 1.70]

#creando una tupla (no se pueden modificar sus elementos y separamos con coma cada elemento)
tupla=("Leonel Torres Rodríguez", "Soy Leo", True, 1.70)

#Esto es válido 
lista[1]="Soy Pilloboy"

#esto no es válido
#tupla[1]="Soy Pilloboy"

#Creando un conjunto (set) (no se accede a elementos por indice, no almacena duplicados)

conjunto={"Leonel Torres Rodríguez", "Soy Leo", True, 1.70}

#printo(conjunto[3])-> no puede acceder al elemento

#Creando un diccionario (dict)(la estructura es key :value y separamos con comas)
diccionario={
    #Clave          #Valor
    "nombre"   :    "Leonel",
    "Apellidos":    "Torres Rodríguez",
    "Anime"    :    "Jojos",
    "esta alterado": True,
    "Edad":          16,
    "Dato_duplicado":"Jojos"
}

print(diccionario["Edad"])
print(lista[0])

