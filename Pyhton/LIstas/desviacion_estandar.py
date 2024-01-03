import math


def desviacion_estandar(valores):
    suma_de_lista = sum(valores)
    numero_de_datos = len(valores)
    promedio = suma_de_lista / numero_de_datos
    suma_cuadrados_diferencias = sum((x - promedio) ** 2 for x in valores)
    varianza = suma_cuadrados_diferencias / numero_de_datos
    desviacion_estandar = math.sqrt(varianza)
    return desviacion_estandar

valores = [1.5, 9.5]
resultado = desviacion_estandar(valores)
print(resultado)

