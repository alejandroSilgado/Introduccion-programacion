def numero_revez(numero,reversed_string):
    numero = int(input("Ingrese un entero de n dígitos: "))# Convertir el número a cadena y luego invertir la cadena
    reversed_string = "".join(reversed(str(numero)))
    return reversed_string

def main(titulo_menu,uno,dos,tres,cuatro,cinco,seis):
    while True:
        print(titulo_menu)
        print(uno)
        print(dos)
        print(tres)
        print(cuatro)
        print(cinco)
        print(seis)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "5":
            pass
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            
file 








