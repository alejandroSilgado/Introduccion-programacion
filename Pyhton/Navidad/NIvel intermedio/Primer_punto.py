def registrar_ciudad(ciudades, cantidad_sismos):
    ciudad = input("Ingrese el nombre de la ciudad: ")
    ciudades[ciudad] = [0] * cantidad_sismos
    print(f"Ciudad {ciudad} registrada con éxito.")

def registrar_sismo(ciudades, ciudad_actual):
    for i in range(len(ciudades[ciudad_actual])):
        sismo = float(input(f"Ingrese el nivel de sismo para la muestra {i + 1} en la ciudad {ciudad_actual}: "))
        ciudades[ciudad_actual][i] = sismo
    print(f"Sismos registrados con éxito para la ciudad {ciudad_actual}.")

def buscar_sismos_por_ciudad(ciudades, ciudad_actual):
    print(f"Sismos registrados en la ciudad {ciudad_actual}: {ciudades[ciudad_actual]}")

def informe_riesgo(ciudades):
    riesgo = {"Amarillo (Sin riesgo)": 2.5, "Naranja (Riesgo medio)": 4.5, "Rojo (Riesgo alto)": float('inf')}

    for ciudad, sismos in ciudades.items():
        promedio = sum(sismos) / len(sismos)
        
        for rango, limite in riesgo.items():
            if promedio < limite:
                print(f"Para la ciudad {ciudad}, el informe de riesgo es: {rango}")
                break

def main():
    ciudades = {}
    cantidad_ciudades = 5
    cantidad_sismos = int(input("Ingrese la cantidad de sismos a registrar por ciudad: "))

    while True:
        print("\n*** Menú ***")
        print("1. Registrar Ciudad")
        print("2. Registrar Sismo")
        print("3. Buscar Sismos por Ciudad")
        print("4. Informe de Riesgo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_ciudad(ciudades, cantidad_sismos)
        elif opcion == "2":
            ciudad_actual = input("Ingrese el nombre de la ciudad para registrar el sismo: ")
            if ciudad_actual in ciudades:
                registrar_sismo(ciudades, ciudad_actual)
            else:
                print(f"La ciudad {ciudad_actual} no ha sido registrada.")
        elif opcion == "3":
            ciudad_actual = input("Ingrese el nombre de la ciudad para buscar los sismos: ")
            if ciudad_actual in ciudades:
                buscar_sismos_por_ciudad(ciudades, ciudad_actual)
            else:
                print(f"La ciudad {ciudad_actual} no ha sido registrada.")
        elif opcion == "4":
            informe_riesgo(ciudades)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
