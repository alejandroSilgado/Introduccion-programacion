palabra = input("Ingrese una palabra: ")
letras_palabra = list(palabra)
extremidades = 5

letras_adivinadas = []

while extremidades > 0:
    letra = input("Ingrese una letra: ")

    if letra in letras_palabra:
        letras_adivinadas.append(letra)
        print("Muy bien, continúa. Letras adivinadas: " + " ".join(letras_adivinadas))
    else:
        extremidades -= 1
        print("Letra incorrecta, te quedan: " + str(extremidades))

    if set(letras_adivinadas) == set(letras_palabra):
        print("¡Felicidades! Has adivinado la palabra.")
        break

if extremidades == 0:
    print("Lo siento, te quedaste sin intentos. La palabra era: " + palabra)
