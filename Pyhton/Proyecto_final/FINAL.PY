import json

def cargar_campers_desde_json():
    try:
        with open("Pyhton/Proyecto_final/camper_data.json", "r") as archivo:
            contenido = archivo.read().strip()
            try:
                campers = json.loads(contenido)
                
                if isinstance(campers, list) and all(isinstance(camper, dict) for camper in campers):
                    campers_dict = {camper['identificacion']: camper for camper in campers}
                    return campers_dict
                else:
                    campers_dict = json.loads(contenido)
                    
                    if isinstance(campers_dict, dict):
                        return campers_dict
                    else:
                        print("Error de formato JSON. No se pudo cargar como diccionario.")
                        return {}
            except json.JSONDecodeError:
                print("Error de formato JSON. No se pudo cargar como lista de diccionarios.")
                return {}
    except FileNotFoundError:
        return {}


def registrar_campers():
    nombres = input("Ingrese el nombre del camper: ")
    apellidos = input("Ingrese el apellido del camper: ")
    identificacion = int(input("Ingrese el documento del camper: "))
    direccion = input("Ingrese la direccion del camper:  ")
    acudiente = input("Ingrese el acudiente del camper: ")
    telefono_celular = int(input("Ingrese el numero celular del camper: "))
    telefono_fijo = int(input("Ingrese el numero fijo del camper: "))
    estado = input("Ingrese el estado del camper: ")

    listas_campers = {
        'nombre': nombres,
        'apellido': apellidos,
        'identificacion': identificacion,
        'direccion': direccion,
        'acudiente': acudiente,
        'telefono_celular': telefono_celular,
        'telefono_fijo': telefono_fijo,
        'estado': estado
    }

    return listas_campers

def guardar_en_json(listas_campers):
    try:
        with open("Pyhton/Proyecto_final/camper_data.json", "a") as archivo:
            archivo.write(json.dumps(listas_campers) + '\n')
        print("Camper registrado exitosamente.")
    except Exception as e:
        print(f"Error al guardar en el archivo JSON: {e}")

def registro_resultado(listas_campers):
    identificacion_a_validar = int(input("Ingrese la identificacion del camper: "))
    
    if identificacion_a_validar in listas_campers:
        camper = listas_campers[identificacion_a_validar]
        
        nota_trabajo_practico = int(input("Ingrese la nota del trabajo practico: "))
        nota_evaluacion_filtro = int(input("Ingrese la nota de la evaluacion del filtro: "))
        nota_trabajo_clase = int(input("Ingrese la nota del trabajo en clase: "))
        
        if nota_trabajo_practico > 0 and nota_evaluacion_filtro > 0 and nota_trabajo_clase > 0:
            porcentaje_60 = float(nota_trabajo_practico * 0.6)
            porcentaje_40 = float(nota_evaluacion_filtro * 0.4)
            porcentaje_10 = float(nota_trabajo_clase * 0.1)
            resultado = float(porcentaje_60 + porcentaje_40 + porcentaje_10)

            camper['nota_final'] = resultado  
            print(f"Resultado registrado para el estudiante {camper['nombre']} {camper['apellido']}.")
        else:
            print("Error: Las notas deben ser mayores a 0")
    else:
        print("El estudiante no se encuentra en la base de datos. Intente de nuevo.")


def resgistro_areas_entrenamiento():
    pass
def asignacion_rutas():
    pass
def gestor_matriculas():
    pass
def evaluacion_campers():
    pass
def entrenadores():
    pass
def reportes():
    pass    

if __name__ == "__main__":
    campers_dict = cargar_campers_desde_json()
    while True:
        print("\n*** Menú ***")
        print("1. Inscribir campers :")
        print("2. Registrar resultado de la prueba :")
        print("3. Registro de Áreas de Entrenamiento:")
        print("4. Asignación a Rutas: ")
        print("5. Gestor de Matrículas:")
        print("6. Evaluación de Campers:")
        print("7. Entrenadores")
        print("8. Reportes")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            a = registrar_campers()
            campers_dict[a['identificacion']] = a
            guardar_en_json(campers_dict)
        elif opcion == "2":
            registro_resultado(campers_dict)
            guardar_en_json(campers_dict)
        elif opcion == "3":
            resgistro_areas_entrenamiento()
        elif opcion == "4":
            asignacion_rutas()
        elif opcion == "5":
            gestor_matriculas()
        elif opcion == "6":
            pass
        elif opcion =="7":
            pass
        elif opcion =="8":
            pass
        elif opcion == "9":
            pass
        else:
            print("Opción no válida. Intente de nuevo.")


