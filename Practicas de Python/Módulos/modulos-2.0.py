#Si el módulo estuviera en una carpeta en la misma ruta
#import Funciones_buenas.saludar as m_saludar

import sys

sys.path.append("c:\\Users\\TORRES RODRÍGUEZ\\Desktop\\Practicas de Python\\Funciones_buenas")

from modulo_saludar import saludar as saludar_normal

print(saludar_normal("Leonel"))
