from datetime import datetime

dia_nacimiento = int(input("Ingrese el día de nacimiento: "))
mes_nacimiento = int(input("Ingrese el mes de nacimiento: "))
año_nacimiento = int(input("Ingrese el año de nacimiento: "))

fecha_actual = datetime.now()

fecha_nacimiento = datetime(año_nacimiento, mes_nacimiento, dia_nacimiento)

if fecha_nacimiento.month < fecha_actual.month or (fecha_nacimiento.month == fecha_actual.month and fecha_nacimiento.day <= fecha_actual.day):
    edad = fecha_actual.year - fecha_nacimiento.year
else:
    edad = fecha_actual.year - fecha_nacimiento.year - 1

print(f"Usted tiene {edad} años.")

