numero_dias = int(input("¿Cuántos datos ingresarás?: "))

lista_datos_ingresados = []

for i in range(1, numero_dias + 1):
    datos_ingresados = float(input(f"Dato {i}: "))
    lista_datos_ingresados.append(datos_ingresados)

numero_datos = len(lista_datos_ingresados)
suma_datos = sum(lista_datos_ingresados)
promedio = suma_datos / numero_datos

mayores_que_promedio = sum(1 for dato in lista_datos_ingresados if dato > promedio)

print(f"El promedio es: {promedio}")
print(f"{mayores_que_promedio} datos son mayores que el promedio.")
