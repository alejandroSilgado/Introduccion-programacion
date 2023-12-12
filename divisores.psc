Algoritmo divisores
	Definir num1,divisor Como Entero
	num1=0
	max_divisores=0
	
	Escribir "ingrese un numero"
	leer num1
	
	Escribir "los divisores de ", num1 " son: ";
	
	Para divisor<-1 Hasta num1 Con Paso 1 Hacer
		si num1 % divisor =0 Entonces
		FinSi
		Escribir divisor
	Fin Para
	
	
FinAlgoritmo
	