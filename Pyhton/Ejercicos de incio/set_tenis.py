def determinar_ganador_set(juegos_A, juegos_B):
    if abs(juegos_A - juegos_B) >= 2 and (juegos_A >= 6 or juegos_B >= 6):
        if juegos_A > juegos_B:
            return "A ganó el set"
        else:
            return "B ganó el set"
    elif juegos_A == 6 and juegos_B == 6:
        return "El set se define en un último juego (7-6)"
    else:
        return "El set aún no ha terminado"

sets_A = 0
sets_B = 0

while sets_A < 2 and sets_B < 2:
    juegos_A = 0
    juegos_B = 0

    while True:
        juegos_A += int(input("Ingrese el número de juegos ganados por A: "))
        juegos_B += int(input("Ingrese el número de juegos ganados por B: "))

        resultado = determinar_ganador_set(juegos_A, juegos_B)
        print(resultado)

        if "ganó el set" in resultado:
            break

    # Incrementa el marcador de sets
    if "A ganó el set" in resultado:
        sets_A += 1
    elif "B ganó el set" in resultado:
        sets_B += 1

    print(f"Marcador de sets: A = {sets_A}, B = {sets_B}")
