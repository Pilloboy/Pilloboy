# Importando un módulo y asignandole el nombre m_saludar
# import modulo_saludar as m_saludar

# Desde el módulo saludar importamos dos funciones y les cambiamos el nombre
from Funciones_buenas.saludar import saludar as saludar_normal, saludar_raro as saludar_como_coscu
import Funciones_buenas.saludar as m_saludar

# Creamos la variables con los saludos
Saludo = saludar_normal("Leonel")
Saludo_raro = saludar_como_coscu("Jhostin")

# Mostramos los resultados
print(Saludo)
print(Saludo_raro)

# Para ver las propiedades y métodos de el namespace
print(dir(m_saludar))

# Accedemos al nombre del módulo llamado
print(m_saludar.__name__)
