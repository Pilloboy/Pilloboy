def fibonacci_lista(num):
    a, b = 0, 1
    fibonacci = [0]
    for i in range(num):
        if b > num:
            return fibonacci,i
        else:
            a, b = b, a+b
            fibonacci.append(a)

Resultado,veces = fibonacci_lista(34)
print(Resultado,veces)
