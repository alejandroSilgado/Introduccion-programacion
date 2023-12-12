Algoritmo notas
	Definir certamen1, certamen2, certamen3, examen, promedio_certamenes Como Real
	
	Escribir "Ingrese la nota del Certamen 1: "
	Leer certamen1
	
	Escribir "Ingrese la nota del Certamen 2: "
	Leer certamen2
	
	Escribir "Ingrese la nota del Certamen 3: "
	Leer certamen3
	
	Escribir "Ingrese la nota del Examen: "
	Leer examen
	
	Si certamen1 < 2 Y certamen2 < 2 Entonces
		Escribir "Estudiante automáticamente reprobado."
	Sino Si certamen1 > 9 Y certamen2 > 9 Entonces
			Escribir "Estudiante automáticamente aprobado."
		Sino
			promedio_certamenes = (certamen1 + certamen2 + certamen3) / 3
			
			Si promedio_certamenes >= 7 Entonces
				Escribir "Estudiante aprobado."
			Sino 
				Si promedio_certamenes < 3 Entonces
					Escribir "Estudiante reprobado."
				Sino
					Si examen >= 5 Entonces
						Escribir "Estudiante aprobado."
					Sino
						Escribir "Estudiante reprobado."
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	FinSi
	


FinAlgoritmo
