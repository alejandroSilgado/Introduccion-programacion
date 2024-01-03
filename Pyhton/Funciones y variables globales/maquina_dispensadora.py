comidaA = 270
comidaB = 340
comidaC = 370
valor10 = 10
valor50 = 50
valor100 = 100
montoTotal = 0
monedasIngresadas = 0
vuelto = 0

productoElegido = input("Elija un producto. Opciones: A(270), B(340), C(390): ")

if productoElegido == "A":
    montoTotal = comidaA
elif productoElegido == "B":
    montoTotal = comidaB
elif productoElegido == "C":
    montoTotal = comidaC

while monedasIngresadas < montoTotal:
    moneda = int(input("Ingrese monedas (10, 50 o 100): "))
    
    if moneda != valor10 and moneda != valor50 and moneda != valor100:
        print("Error: Ingrese solo monedas de 10, 50 o 100.")
        monedasIngresadas -= moneda

    monedasIngresadas += moneda

vuelto = monedasIngresadas - montoTotal

if vuelto > 0:
    print("Monto pagado. Su vuelto es de", vuelto, "pesos.")
else:
    print("Monto pagado. No hay vuelto.")