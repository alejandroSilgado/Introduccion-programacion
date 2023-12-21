import math

muestras = [
    ("Pedro", "00000101010101010101"),
    ("Juan", "00101010101101110111"),
    ("Diego", "00100010010000001001"),
]

cromosomas_ingresados = input("Ingrese la secuencia de cromosomas: ")
lista_porcentaje = []

for i in range (len(muestras)):
    nombre, cromosomas_muestra = muestras[i]
    coincidencias = sum(c1 == c2 for c1, c2 in zip(cromosomas_ingresados, cromosomas_muestra))
    porcentaje_similitud = (coincidencias / len(cromosomas_ingresados)) * 100
    lista_porcentaje.append(porcentaje_similitud)

indice_max = lista_porcentaje.index(max(lista_porcentaje))
print(f"\nEl mayor porcentaje de similitud fue con {muestras[indice_max][0]} ({max(lista_porcentaje):.2f}%).")
