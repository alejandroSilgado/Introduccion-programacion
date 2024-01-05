def registrar_productos():
    codigo = int(input("Ingrese el código del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    valor_compra = float(input("Ingrese el valor de compra del producto: "))
    valor_venta = float(input("Ingrese el valor de venta del producto: "))
    stock_minimo = int(input("Ingrese stock mínimo del producto: "))
    stock_maximo = int(input("Ingrese stock máximo del producto: "))
    nombre_proveedor = input("Ingrese el nombre del proveedor del producto: ")

    producto = {
        'nombre': nombre,
        'codigo': codigo,
        'valor_compra': valor_compra,
        'valor_venta': valor_venta,
        'stock_minimo': stock_minimo,
        'stock_maximo': stock_maximo,
        'nombre_proveedor': nombre_proveedor
    }
    return producto

def visualizacion_productos(producto):
    print(producto)

def actualizaciones_stock(producto):
    codigo_validacion = int(input("Ingrese el código del producto: "))
    if codigo_validacion in producto:
        operacion = input("¿Vas a sumar o a restar el stock? (Responde suma o resta): ")
        if operacion == "suma":
            i = int(input("Ingrese el valor a sumar: "))
            producto[codigo_validacion]['stock_minimo'] += i
        elif operacion == "resta":
            i = int(input("Ingrese el valor a restar: "))
            producto[codigo_validacion]['stock_minimo'] -= i
        else:
            print("Operación no válida.")
    else:
        print("Código de producto no encontrado.")

def info_puntos_criticos(producto, productos_criticos):
    if producto['stock_minimo'] < productos_criticos:
        print(producto)

def calculo_ganancia(producto, ganancia):
    # Asumiendo que deseas calcular la ganancia de alguna manera, ajusta esta fórmula según tus necesidades
    ganancia = producto['valor_venta'] - producto['valor_compra']
    print("Su ganancia es:", ganancia)

def main():
    a = None  # Inicializar a fuera del bucle
    while True:
        print("\n*** Menú ***")
        print("1. Registrar e:")
        print("2. Visualización de Productos:")
        print("3. Actualización de Stock:")
        print("4. Informe de Productos Críticos")
        print("5. Cálculo de Ganancia Potencial")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            a = registrar_productos()
        elif opcion == "2":
            visualizacion_productos(a)
        elif opcion == "3":
            if a is not None:  # Verificar que 'a' no sea None antes de llamar a actualizaciones_stock
                actualizaciones_stock(a)
            else:
                print("Primero registra un producto antes de actualizar el stock.")
        elif opcion == "4":
            info_puntos_criticos(a, 10)  # Ingresa el valor mínimo deseado para considerar como crítico
        elif opcion == "5":
            calculo_ganancia(a, 0)  # Ingresa el valor deseado para calcular la ganancia
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
