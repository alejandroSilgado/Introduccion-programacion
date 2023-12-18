numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
numero4 = int(input("Ingrese el cuarto número: "))

numeros_ordenados = sorted([numero1, numero2, numero3, numero4])

print("Números ordenados:", ' '.join(map(str, numeros_ordenados)))
