Algoritmo LargoPalabras
    definir palabra1, palabra2 Como Caracter
    definir largoPalabra1, largoPalabra2 Como Entero
    
    escribir "Digite la primera palabra: ";
    leer palabra1
    escribir "Digite la segunda palabra: ";
    leer palabra2 
    
    largoPalabra1 <- Longitud(palabra1)
    largoPalabra2 <- Longitud(palabra2)
    
    si largoPalabra1 > largoPalabra2 Entonces
        escribir "La primera palabra es más larga por ", largoPalabra1-largoPalabra2, " letras"
    sino 
        escribir "La segunda palabra es más larga por ", largoPalabra2-largoPalabra1, " letras"
    FinSi
	
FinAlgoritmo

