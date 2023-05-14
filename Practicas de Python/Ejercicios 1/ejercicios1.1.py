#Promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Duración de crudo
crudo_promedio = 5
crudo_dalto = 3.5

#Diferencias de duración
diferencia_con_min = 100 - (dalto_curso / otros_cursos_min * 100)
diferencia_con_max = round(100 - (dalto_curso / otros_cursos_max  * 100),1)
diferencia_con_promedio = 100 - (dalto_curso / otros_cursos_promedio * 100)

#Calcular el porcentaje de tiempo vacio
tiempo_vacio_promedio = round(100 - otros_cursos_promedio / crudo_promedio * 100, 1)
tiempo_vacio_dalto = round(100 - dalto_curso  / crudo_dalto * 100, 1)

#Mostrando las diferencias de duración
print("---------------")
print ("El curso de Dalto dura:")
print (f" - un {diferencia_con_min}""% menos que el curso más rápido")
print (f" - un {diferencia_con_max}""% menos que el curso más lento")
print (f" - un {diferencia_con_promedio}""% menos que el promedio")
print("---------------")

#Mostrando la cantidad de espacios vacios que se remueven (ejercicio b)
print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio" )
print(f"El curso de Dalto elimina un {tiempo_vacio_dalto}% de tiempo vacio") 
print("---------------")

#Mostrando diferencias si los cursos duraran 10 horas
print(f"Ver 10 horas de este curso equivale a ver  {round(otros_cursos_promedio / dalto_curso * 10,1)}horas de otros cursos")
print(f"Ver 10 horas de otro curso equivale a ver  {round(dalto_curso / otros_cursos_promedio * 10,1)}horas del curso de Dalto")
print("---------------")