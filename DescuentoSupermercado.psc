Algoritmo DescuentoSupermercado
    Definir n, cantidadProductos Como Entero
    Definir precio, precioTotal, descuentoTotal Como Real
    
    Escribir "Ingrese el valor de n:"
    leer n
    
    Escribir "Ingrese la cantidad de productos:"
    leer cantidadProductos
    
    precioTotal = 0
    descuentoTotal = 0
    
    Para i <- 1 Hasta cantidadProductos Hacer
        Escribir "Ingrese el precio del producto ", i
        leer precio
        
        Si (i <= n) Entonces
            descuento =descuento+ precio * 0.2
			escribir descuento;
		FinSi
		
        Si i>n y i<=n*2
            descuento =descuento+ precio * 0.1 
			escribir descuento;
        Fin Si
		si i>n*2 y i>=n*3
			descuento=descuento+precio*0.05
			escribir descuento;
		FinSi
        
        descuentoTotal = descuentoTotal + descuento
        precioTotal = precioTotal + precio
    Fin Para
    
    Escribir "Total:", precioTotal
    Escribir "Descuento:", descuento
    Escribir "Por pagar:", precioTotal - descuento
    
FinAlgoritmo

