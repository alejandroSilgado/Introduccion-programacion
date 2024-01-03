numero = int(input("Ingrese un entero de dígitos: "))

rev = "".join(reversed(str(numero)))

rev_entero = int(rev)

if rev_entero == numero:
    print("Es palíndromo")
else:
    print("No es palíndromo")
