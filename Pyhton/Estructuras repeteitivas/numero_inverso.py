# Solicitar al usuario un entero de n dígitos
numero = int(input("Ingrese un entero de n dígitos: "))

# Verificar que el número sea positivo
if numero > 0:
    # Invertir el número utilizando cadenas
    numero_inverso = int(str(numero)[::-1])

    # Mostrar el resultado
    print("Número con los dígitos en orden inverso:", numero_inverso)
else:
    print("Por favor, ingrese un número positivo.")
    