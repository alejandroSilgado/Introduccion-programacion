import math
def calculardigito(numero_al_revez ,digitos_numero) :
    suma=0
    for i in range (2,digitos_numero+2) :
        if i<=7 :
            suma=suma+(int(numero_al_revez[i-2])*i)
        elif i>7:
            suma=suma+(int(numero_al_revez[i-2])*i-6)
    return suma
suma=0
digito=0

numero = str(int(input("Ingrese un numero de  dígitos: ")))
digitos_numero= len(numero)
numero_al_revez = "".join(reversed(str(numero)))
digito=calculardigito(numero_al_revez ,digitos_numero)
modulo=digito%11
codigo=11-modulo

print(numero,"-",codigo)

    






