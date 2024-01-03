Algoritmo PotenciasDeDos
	Definir limite_superior,exponente,resultado Como Entero
	limite_superior=0
	
    Escribir "Ingrese el exponente máximo para las potencias de 2: "
    Leer limite_superior
	
    Para exponente <- 0 Hasta limite_superior Con Paso 1 Hacer
        resultado <- 2 ^ exponente
        Escribir "2^", exponente, " = ", resultado
    FinPara
FinAlgoritmo
