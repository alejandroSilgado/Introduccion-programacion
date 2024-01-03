cantidad_peso_ideal = 0
cantidad_obesidad_I = 0
cantidad_obesidad_II = 0
cantidad_obesidad_III = 0
cantidad_sobrepeso = 0

numero_estudiantes = int(input("Cuantos estudiantes se van a registrar?: "))

for _ in range(numero_estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    peso = float(input("Ingrese el peso del estudiante (en kg): "))
    altura = float(input("Ingrese la altura del estudiante (en metros): "))

    IMC = peso / altura**2

    if 18.5 <= IMC < 24.9:
        cantidad_peso_ideal += 1
    elif 30 <= IMC < 34.9:
        cantidad_obesidad_I += 1
    elif 35 <= IMC < 39.9:
        cantidad_obesidad_II += 1
    elif IMC >= 40:
        cantidad_obesidad_III += 1
    elif 25 <= IMC < 29.9:
        cantidad_sobrepeso += 1

print("\nInforme de Salud Estudiantil:")
print(f"a. Estudiantes en peso ideal: {cantidad_peso_ideal}")
print(f"b. Estudiantes en obesidad grado I: {cantidad_obesidad_I}")
print(f"c. Estudiantes en obesidad grado II: {cantidad_obesidad_II}")
print(f"d. Estudiantes en obesidad grado III: {cantidad_obesidad_III}")
print(f"e. Estudiantes en Sobrepeso: {cantidad_sobrepeso}")

