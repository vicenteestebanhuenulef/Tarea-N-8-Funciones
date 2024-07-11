def sumatoria(numero):
    if numero == 0:
        return 0
    else:
        return numero + sumatoria(numero - 1)
     
numero = 12
res = sumatoria(numero)
print(f"La sumatoria de {numero} es: {res}")