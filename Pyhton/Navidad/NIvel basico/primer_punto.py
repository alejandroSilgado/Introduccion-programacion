numeros = []
for i in range(3):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

resultado_suma=sum(numeros)

print("La suma de los numeros es: ", resultado_suma)
