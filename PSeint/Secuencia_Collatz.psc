Algoritmo Secuencia_Collatz
	Definir num, i, resultado Como Entero
	num=0
	Escribir "escriba un numero para darle la secuencia de collatz"
	leer num 
	
	Mientras num <>1  Hacer
	
        Si num%2 = 0 Entonces
            num = num / 2
        SiNo
            num = 3 * num + 1
        Fin Si
        Escribir num
    Fin Mientras

	
FinAlgoritmo
