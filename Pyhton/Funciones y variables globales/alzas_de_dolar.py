num_dias = int(input("¿Cuántos días?: "))
precio_anterior = 0
mayor_alza = 0

for i in range(1, num_dias + 1):
    precio_dia = float(input("Día " + str(i) + ": "))  # Convierte la entrada a un número de punto flotante
    if i > 1:
        if (precio_dia - precio_anterior) > mayor_alza:
            mayor_alza = precio_dia - precio_anterior
    precio_anterior = precio_dia

if num_dias == 1:
    print("No hubo alzas")
else:
    print("La mayor alza fue " + str(round(mayor_alza, 1)))
