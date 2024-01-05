def registrar_campers():
    nombres = input("Ingrese el nombre del camper: ")
    apellidos = input("Ingrese el apellido del camper: ")
    identificacion = int(input("Ingrese el documento del camper: "))
    direccion = input("Ingrese la direccion del camper: ")
    acudiente = input("Ingrese el acudiente del camper: ")
    telefono_celular = int(input("Ingrese el numero celular del camper: "))
    telefono_fijo = int(input("Ingrese el numero fijo del camper: "))
    estado = input("Ingrese el estado del camper: ")

    lista_camper = {
        'nombre': nombres,
        'apellido': apellidos,
        'identificacion': identificacion,
        'direccion': direccion,
        'acudiente': acudiente,
        'telefono_celular': telefono_celular,
        'telefono_fijo': telefono_fijo,
        'estado': estado
    }
    return lista_camper

def registrar_prueba(lista_camper):
    identificacion_a_validar = input("Ingresa el numero de identifiacion")
    
    if identificacion_a_validar == 
        nota_trabajo_practico = float(input("Ingrese la nota del trabajo practico: "))
        nota_evaluacion_filtro = float(input("Ingrese la nota de la evaluacion del filtro: "))
        nota_trabajo_clase = float(input("Ingrese la nota del trabajo en clase: "))
        porcentaje_60=nota_trabajo_practico*0.6
        porcentaje_40=nota_evaluacion_filtro*0.6
        porcentaje_10=nota_trabajo_clase*0.4
        resultado=porcentaje_60+porcentaje_40+porcentaje_10
        if resultado>= 60:
            print("El estudiante pasó la prueba")
        else:
            print("El estudiante no pasó la prueba")
    else:
        print("El estudiante no está inscrito. No se puede registrar la prueba.")

def main():
    campers_list = []

    while True:
        print("\n*** Menú ***")
        print("1. Inscribir campers :")
        print("2. Registrar resultado de la prueba :")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            camper = registrar_campers()
            campers_list.append(camper)
        elif opcion == "2":
            identificacion_a_validar = int(input("Ingrese la identificacion del camper: "))
            found_camper = next((c for c in campers_list if c['identificacion'] == identificacion_a_validar), None)
            
            if found_camper:
                registrar_prueba(found_camper)
            else:
                print("El estudiante no se encuentra en la base de datos, intente de nuevo.")
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
