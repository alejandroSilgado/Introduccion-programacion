Algoritmo alzas_dolar
	Definir num_dias como entero
	definir precioDia como real 
	Definir precio_anterior como entero 
	definir mayor_alza como entero 
	num_dias=0
	precioDias=0
	precio_anterior = 0
    mayor_alza = 0
	
	Escribir "Cuantos dias se contaron? : "
	leer num_dias
	
	Para x<-1 Hasta num_dias Con Paso 1 Hacer
		Escribir "Dia ",x ":"
		leer precioDia
	Fin Para
	
	Si x > 1 Entonces
		Si (precioDia - precio_anterior) > mayor_alza Entonces
			mayor_alza = precioDia - precio_anterior
		Fin Si
	Fin Si
	
	precio_anterior = precioDia

Si num_dias = 1 Entonces
	Escribir "No hubo alzas."
Sino
	Escribir "La mayor alza fue de ", mayor_alza;
Fin Si

FinAlgoritmo
