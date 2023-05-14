#Forma no óptima de sumar valores
#def suma (lista):
#    numeros_sumados = 0
#    for numero in lista:
#    numeros_sumados = numeros_sumados + numero
#    return numeros_sumados 

#resultado = suma([5,9,7])
#print(resultado)

#Forma óptima de sumar valores
def suma_total (numeros):
    return sum([*numeros])

resultado2 = suma_total([5,9,7])
print(resultado2)

#Lo mismo de de arriba pero utilizando el parámetro * como parametro (*args)
def suma (nombre,*numeros):
    return f"{nombre} la suma de tus numeros es: {sum(numeros)}"

resultado = suma("Leonel", 5,9,7)
print(resultado)

