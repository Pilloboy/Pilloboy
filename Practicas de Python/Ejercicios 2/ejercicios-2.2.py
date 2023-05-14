# Creando una función que nos devuelva los numeros primos
# Entre 0 y el número que pasamos

# Crear una función que verifique si un número es primo.
def es_primo(num):
    # Verificamos que el número pasado no pueda dividirse
    # por ningún número entre 2 y ese mismo número.
    for Numero in range(num):
        if num % 2 == 0:
            return False
        else:
            Numero = True
            return Numero 
        


def primos_hasta(num):
    primos = []
    for i in range(3, num-1):
        resultado = es_primo(i)
        if resultado == True:
            primos.append(i)
    return primos


resultado1 = primos_hasta(13)

print(resultado1)
