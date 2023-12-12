Algoritmo maquina_alimentos 
    Definir comidaA, comidaB, comidaC, monedasIngresadas, montoTotal, vuelto Como Real
    Definir valor10, valor50, valor100 Como Entero
    Definir productoElegido Como Caracter
    valor10 = 10
    valor50 = 50
    valor100 = 100
    comidaA = 270
    comidaB = 340
    comidaC = 370
    vuelto = 0
    
    Escribir "Elija un producto. Opciones: A, B, C"
    leer productoElegido
    
    Si productoElegido = "A" Entonces
        montoTotal = comidaA
    Sino
        Si productoElegido = "B" Entonces
            montoTotal = comidaB
        Sino
            Si productoElegido = "C" Entonces
                montoTotal = comidaC
            Fin Si
        Fin Si
    Fin Si
    
    Mientras monedasIngresadas < montoTotal Hacer
        Escribir "Ingrese monedas (10, 50 o 100)"
        leer moneda
        monedasIngresadas = monedasIngresadas + moneda
        
        Si moneda <> valor10 Y moneda <> valor50 Y moneda <> valor100 Entonces
            Escribir "Error: Ingrese solo monedas de 10, 50 o 100."
            monedasIngresadas = monedasIngresadas - moneda 
        Fin Si
    Fin Mientras
    
    vuelto = monedasIngresadas - montoTotal
    
    Si vuelto > 0 Entonces
        Escribir "Monto pagado. Su vuelto es de ", vuelto, " pesos."
    Sino
        Escribir "Monto pagado. No hay vuelto."
    Fin Si
    
FinAlgoritmo

