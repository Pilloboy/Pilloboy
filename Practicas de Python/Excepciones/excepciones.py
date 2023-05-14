#Creando función que suma números 
def sum():
    while True:
        #Pidiendo números
        a = input("Numero1: ")
        b =input("Numero2: ")
        #Intentando convertirlos a enteros y sumarlos
        try:
            resultado = int(a) + int(b)   
        #Si lanzo una excepción pedirle que aingrese los datos 
        except ValueError as e:
            print("Por favor no te detengas")
            print(F"ERROR: {e}")
        #Si todo salio bien terminams el bucle
        else:
            break
        #Finally se ejecuta siempre
        finally:
            print("Esto se ejecuta siempre")
    #Mostrando el resultado
    return resultado

print(sum())