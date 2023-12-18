hora_actual = int(input("Ingrese la hora actual: "))
horas_a_sumar = int(input("Cantidad de horas: "))

nueva_hora = (hora_actual + horas_a_sumar) % 24


print("En "+str(horas_a_sumar)+" horas, el reloj marcara las "+str(nueva_hora))
