def separar(lista):
    pares = []
    impares = []
    
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    pares.sort()
    impares.sort()
    
    return pares, impares
    
num = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]
pares, impares = separar(num)
print("Números pares:", pares)
print("Números impares:", impares)