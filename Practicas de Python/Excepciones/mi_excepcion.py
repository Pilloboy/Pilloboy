class MiExcepción(Exception):
    def __init__(self,err): 
            print(f"Cometiste el siguiente error: {err}")
            
#Lanzando mi propia excepción
#raise MiExcepción ("Te digo, vivir no es lo tuyo")

#Manejandola
#try:
#    raise MiExcepción ("Te digo, vivir no es lo tuyo")
#except:
#    print("Impresionante, eres pendejo")
    