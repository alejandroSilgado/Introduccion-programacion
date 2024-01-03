ingresados = []
lista_pares = []
lista_impares = []
menores_10 = []
entre_20_50 = []
mayores_100 = []

while True:
    numero = int(input("Ingrese un número (ingrese un número negativo para finalizar): "))
    
    if numero < 0:
        break
    
    ingresados.append(numero)

cantidad_elementos = len(ingresados)
numeros_pares = 0  
numeros_impares = 0
resultado_menores = 0
resultado_20_50 = 0
resultado_mayores = 0

for i in range(cantidad_elementos):
    if ingresados[i] % 2 == 0:
        numeros_pares += 1
        lista_pares.append(ingresados[i])
    else:
        numeros_impares += 1
        lista_impares.append(ingresados[i])

    if ingresados[i] < 10:
        menores_10.append(ingresados[i])
    elif 20 <= ingresados[i] <= 50:
        entre_20_50.append(ingresados[i])
    elif ingresados[i] > 100:
        mayores_100.append(ingresados[i])

resultado_menores = len(menores_10)
resultado_20_50 = len(entre_20_50)
resultado_mayores = len(mayores_100)

if numeros_pares > 0:
    promedio_pares = sum(lista_pares) / numeros_pares
else:
    promedio_pares = 0

if numeros_impares > 0:
    promedio_impares = sum(lista_impares) / numeros_impares
else:
    promedio_impares = 0

print("Total de números ingresados:", cantidad_elementos)
print("Total de números pares ingresados:", numeros_pares)
print("Promedio de los números pares:", promedio_pares)
print("Total de números impares ingresados:", numeros_impares)
print("Promedio de los números impares:", promedio_impares)
print("Cuantos números son menores que 10:", resultado_menores)
print("Cuantos números están entre 20 y 50:", resultado_20_50)
print("Cuantos números son mayores que 100:", resultado_mayores)
