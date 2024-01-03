tiempo_viaje=int(input("ingrese la duracion de su tramo: "))
tiempo=tiempo_viaje

while tiempo_viaje : 
    tiempo_viaje=int(input("ingrese la duracion de su tramo: "))
    tiempo=tiempo + tiempo_viaje

horas=int(tiempo//60)
minutos=int(tiempo%60)

print("Tiempo total del viaje fue "+str(horas)+":"+str(minutos))


