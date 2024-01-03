Algoritmo TablasMultiplicar
    Definir numUsuario Como Entero
    numUsuario = 0
    
    Escribir "Ingrese un número en la escala de (1-10)"
    Leer numUsuario
    
    Mientras numUsuario < 1 O numUsuario > 10 Hacer
        Escribir "Ingrese un número válido en la escala de (1-10)"
        Leer numUsuario
    FinMientras
	
    Para i <- 1 Hasta 10 Con Paso 1 Hacer
        Escribir numUsuario, " x ", i, " = ", numUsuario * i
    FinPara
	
FinAlgoritmo
