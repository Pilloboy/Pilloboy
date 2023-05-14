# DATO . MÉTODO ()
cadena1 = "Hola_Soy_Leonel"
cadena2 = "Bienvenido makina"

#Convierte a mayusculas 
mayusc = cadena1.upper()

#Convierte a minusculas
minusc = cadena1.lower()

#Primera letra en mayuscula y las demás las intercambia a minusculas 
primera_letra_mayuscula = cadena1.capitalize()

#Buscamos una cadena en otra cadena, sino hay coincidencias nos devuelve -1
busqueda_find = cadena1.find("L")

#Buscamos una cadena en otra cadena, sino hay coincidencias lanza una excepción 
busqueda_index = cadena1.index("L")

#Si es númerico devuelve True, sino False
es_numerico = cadena1.isnumeric()

#Si es alfanumerico devolvemos True, sino devolvemos False
es_alfanumerico = cadena1.isalpha()

#Contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de veces de coincidencias 
contar_coincidencias = cadena1.count("HolaSoyLeonel")

#Contamos cuantos carácteres tiene una cadena 
contar_caracteres = len(cadena1)

#Verificamos si una cadena empieza con otra cadena dada, si es así devuelve True 
empieza_con = cadena1.startswith("H")

#Verificamos si una cadena termina con otra cadena dada, si es así devuelve True
termina_con = cadena1.endswith("Leonel")

#Si el valor 1, se encuentra en la cadena original, remplaza el valor 1  de la misma, por el valor 2
cadena_nueva = cadena1.replace(","," ")

#Separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split("_")

print(cadena_separada)
