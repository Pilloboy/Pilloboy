#Forma no optima de sumar valores
def suma (lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados
        
resultado = suma([1,2,3,4])
print(resultado)

#Forma optima de sumar valores
def suma (lista):
    return sum([*lista])

resultado2 = suma([1,2,3,4])
print(resultado2)

#Lo mismo que arriba pero utilizando el operador * como argumento (*args)
def suma (nombre,*lista):
    return f"{nombre} la suma de tus números es: {sum(lista)}"

resultado3 = suma("Leonel",1,2,3,4)
print(resultado3)

