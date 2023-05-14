#Creando un conjunto con set()
conjunto = set(["Leonel","Vanessa", 16])

#Metiendo un conjunto dentro de otro conjunto 
conjunto1 = frozenset([1,3,5,7])
conjunto2 = {conjunto1,2,4,6,8}

print(conjunto2)

#Teoría de conjunto
conjunto1 = {1,3,5,7}
conjunto2 = {8,9}

#Verificando si es un subconjunto
print(conjunto2.issubset(conjunto1))
print(conjunto2 <= conjunto1)

#Verificando si es un superconjunto
print(conjunto1.issuperset(conjunto2))
print(conjunto1 > conjunto2)

#Verificar si hay algún número en común
print(conjunto2.isdisjoint(conjunto1))