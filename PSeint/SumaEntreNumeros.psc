Algoritmo SumaEntreNumeros
    Definir num1, num2, suma, i Como Entero
    
    Escribir "Ingrese el primer número: "
    Leer num1
    Escribir "Ingrese el segundo número: "
    Leer num2
    
    Si num1 > num2 Entonces
        Escribir "Error: El primer número debe ser menor o igual al segundo número."
    Sino
        suma <- 0
        
        Para i <- num1 Hasta num2 Con Paso 1 Hacer
            suma <- suma + i
        FinPara
		
		
        Escribir "La suma de los números en el rango [", num1, ", ", num2, "] es: ", suma
    FinSi
FinAlgoritmo
