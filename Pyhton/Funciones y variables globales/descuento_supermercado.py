# Algoritmo DescuentoSupermercado

import math

# Definir variables
n = int(input("Ingrese el valor de n: "))
cantidadProductos = int(input("Ingrese la cantidad de productos: "))
precioTotal = 0
descuentoTotal = 0

# Bucle para ingresar precios y calcular descuentos
for i in range(1, cantidadProductos + 1):
    precio = float(input(f"Ingrese el precio del producto {i}: "))
    descuento = 0

    # Calcular descuento según la categoría del producto
    if i <= n:
        descuento = precio * 0.2
    else:
        grupos_adicionales = math.ceil(i / n) - 1
        descuento = precio * (0.1 ** grupos_adicionales)

    descuentoTotal += descuento
    precioTotal += precio

    print(f"Descuento aplicado para el producto {i}: {descuento}")

# Redondear el precio final hacia abajo
precioFinal = precioTotal - descuentoTotal
precioFinal = math.floor(precioFinal)

# Mostrar resultados
print("Total:", precioTotal)
print("Descuento Total:", descuentoTotal)
print("Precio Final después de aplicar descuento:", precioFinal)

# Fin del algoritmo

