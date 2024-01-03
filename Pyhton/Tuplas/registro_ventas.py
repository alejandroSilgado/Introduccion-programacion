import math

ventas = [
    ("ProductoA", 10, 150),
    ("ProductoB", 5, 200),
    ("ProductoA", 8, 120),
    ("ProductoC", 12, 80),
    ("ProductoB", 3, 210),
    ("ProductoA", 15, 130),
    ("ProductoC", 7, 85),
]

total_ventas = {
    "ProductoA": 0,
    "ProductoB": 0,
    "ProductoC": 0,
}

producto_mas_vendido = {"nombre": "", "cantidad": 0}

for i in range(len(ventas)):
    nombre_producto, cantidad, precio = ventas[i]
    
    if cantidad > producto_mas_vendido["cantidad"]:
        producto_mas_vendido["nombre"] = nombre_producto
        producto_mas_vendido["cantidad"] = cantidad

    if nombre_producto == "ProductoA":
        total_ventas["ProductoA"] += cantidad * precio
    elif nombre_producto == "ProductoB":
        total_ventas["ProductoB"] += cantidad * precio
    elif nombre_producto == "ProductoC":
        total_ventas["ProductoC"] += cantidad * precio

ganancia_total = sum(total_ventas.values())

print("Su total de ventas según cada producto es:", total_ventas)
print("Su ganancia total es:", ganancia_total)
print("El producto más vendido es:", producto_mas_vendido["nombre"], "con una cantidad de:", producto_mas_vendido["cantidad"])
