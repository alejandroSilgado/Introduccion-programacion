Algoritmo  OrdenarTresDigitos

    definir digito1, digito2, digito3, temp como entero 
	
	
    escribir("Ingrese el primer dígito: ")
    leer digito1
    
    escribir("Ingrese el segundo dígito: ")
    leer digito2
	
    escribir("Ingrese el tercer dígito: ")
    leer digito3
	
    si digito1 > digito2 entonces
        temp <- digito1
        digito1 <- digito2
        digito2 <- temp
	FinSi

	si digito2 > digito3 entonces
		temp <- digito2
		digito2 <- digito3
		digito3 <- temp
	FinSi
		
	si digito1 > digito2 entonces
		temp <- digito1
		digito1 <- digito2
		digito2 <- temp
	FinSi
	
	escribir "Dígitos ordenados de menor a mayor: ", digito1, ", ", digito2, ", ", digito3 

FinAlgoritmo


