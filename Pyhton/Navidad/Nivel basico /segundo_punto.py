nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
peso = float(input("Ingrese su peso (en kg): "))
altura = float(input("Ingrese su altura (en metros): "))

IMC = peso / altura**2

print(f"{nombre}, su índice de masa corporal (IMC) es: {IMC:.2f}")

if IMC < 18.5:
    print("Usted está bajo peso.")
elif 18.5 <= IMC < 24.9:
    print("Usted tiene un peso normal.")
elif 25 <= IMC < 29.9:
    print("Usted tiene sobrepeso.")
elif 30 <= IMC < 34.9:
    print("Usted tiene obesidad I.")
elif 35 <= IMC < 39.9:
    print("Usted tiene obesidad II.")
else:
    print("Usted tiene obesidad III.")

