numeros = [1,2,3,4,5,6,7,8,9]

#Creando una función lambda para multiplicarpor dos 
multiplicar_por_dos = lambda x: x*2
print(multiplicar_por_dos(numeros))
#Creando función común que diga si es par o no 
def es_par(num):
    if (num%2==0):
        return True
    
#Usando filter con una función común
numeros_pares = filter(es_par,numeros)

print(list(numeros_pares))
