proceso CalculadoraBasica
    // Declaraci�n de variables
    definir numero1, numero2, resultado como real
    definir operador como caracter
	
    // Entrada de datos
    escribir("Ingrese el primer n�mero: ")
    leer numero1
    
    escribir("Ingrese el segundo n�mero: ")
    leer numero2
	
    escribir("Ingrese el operador (+, -, *, /): ")
    leer operador
	
    // Proceso de c�lculo y salida
    segun operador
        "+" : resultado <- numero1 + numero2
        "-" : resultado <- numero1 - numero2
        "*" : resultado <- numero1 * numero2
        "/" : si numero2 <> 0 entonces
                resultado <- numero1 / numero2
            sino
                escribir("Error: No se puede dividir por cero.")
			FinSi
			otro : escribir("Operador no v�lido.")
		FinSegun
	//resultado final 
	escribir "Tu resultado es: ", resultado
					
FinProceso

