import re

texto = """Hola maestro. esta es la cadena 1. como estas mi capitan
Esta es la segunda linea 2 de texto.
Y Esta es la final (linea 3) definitiva mi capitan"""

# Haciendo una husqueda simple
resultado = re.findall("Esta", texto, flags=re.IGNORECASE)

# \d -> busca dígitos numericos del 0 -> 9
resultado = re.findall(r"\d", texto)


# \D ->busca TODO MENOS dígitos numericos del 0 -> 9
resultado = re.findall(r"\D", texto)


# \w -> busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\w", texto)


# \w -> busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\W", texto)

# \s -> busca espacios en blanco -> tabs, saltos en linea
resultado = re.findall(r"\s", texto)

# \S -> busca TODO MENOS espacios en blanco -> tabs, saltos en linea
resultado = re.findall(r"\S", texto)

# . -> Busca TODO MENOS saltos en linea
resultado = re.findall(r".", texto)

# \n -> Busca saltos en linea
resultado = re.findall(r"\n", texto)

# \ -> Cancelar caracteres especiales, cancelando la función del punto y buscando puntos
resultado = re.findall(r"\.", texto)

# Armando una cadena que busque un numero, seguido de un punto y un espacio
resultado = re.findall(r"\d\.\s", texto)

# ^ -> Busca el comienzo de una linea, buscando Hola al principio de una linea
resultado = re.findall(r"^Hola", texto)

# flags=re.M activa la multiple linea
resultado = re.findall(r"^Esta", texto, flags=re.M)

print(resultado)
