Ingreso_mensual = 84000
Gasto_mensual = 80000

#If anidados y else if (elif)

if Ingreso_mensual >10000:
    if Ingreso_mensual - Gasto_mensual < 0:
        print("Estas en deficit")
    elif Ingreso_mensual - Gasto_mensual > 3000:
        print("Bien, te envidio")
    else:
        print("Estas gastando un chorro")
        
elif Ingreso_mensual > 1000:
    print("Estas bien económicamente en latinoamerica")
    
elif Ingreso_mensual > 500:
    print("Estas bien económicamente en Argentina")
    
elif Ingreso_mensual > 200:
    print("Estas bien económicamente en Venezuela")

else:
    print("Eres pobre")
    