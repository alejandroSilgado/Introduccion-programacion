estatura = float(input("Ingrese la estatura en metros: "))
peso = float(input("Ingrese el peso en kilos: "))
edad = int(input("Ingrese la edad: "))

imc = peso / (estatura ** 2)

if edad < 45:
    if imc < 22.0:
        riesgo = "Bajo"
    elif 22.0 <= imc <= 24.9:
        riesgo = "Moderado"
    else:
        riesgo = "Alto"
else:
    if imc < 22.0:
        riesgo = "Moderado"
    elif 22.0 <= imc <= 24.9:
        riesgo = "Alto"
    else:
        riesgo = "Muy Alto"

print(f"La condición de riesgo es: {riesgo}")
