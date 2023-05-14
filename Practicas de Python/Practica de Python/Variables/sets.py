#Creando un conjunto con set
conjunto = set(["Leonel", "Torres Rodríguez", 16])

#Metiendo un conjunto dentro de otro conjunto 
conjunto1 = frozenset(["Leonel", "Torres Rodríguez", 16])
conjunto2 = {conjunto1, "Vanessa"}
print(conjunto2)

#Teoría de conjuntos

conjunto1 = {1,2,3,4}
conjunto2 = {1,2,4}

#Verificar que es un superconjunto
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto1 > conjunto2

#Verificar que es un sub conjunto
resultado2 = conjunto2.issubset(conjunto1)
resultado2= conjunto2 <= conjunto1

#Verificar si hay un elemento en común
resultado = conjunto1.isdisjoint(conjunto2)

print(resultado)