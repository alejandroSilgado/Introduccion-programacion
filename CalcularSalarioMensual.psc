Algoritmo CalcularSalarioMensual
	
	// Declaracion de variables
	Definir horasTrabajadas como entero
	Definir precioHora  Como Real
	Definir nombre Como Caracter
	definir horasExtras Como entero 
	Definir salario Como real
	definir salarioExtras como real 
	definir salarioBase como real 
	horasTrabajadas=0
	precioHora=0
	nombre=""
	
	Escribir "Ingrese el nombre:";
	leer nombre 
	Escribir "Ingrese el horas trabajadas";
	leer horasTrabajadas
	escribir "ingrese el precio de las horas:";
	leer precioHora
	
	si horasTrabajadas>40 Entonces
		horasExtras<-horasTrabajadas-40;
		salarioExtras<-horasExtras*(precioHora*1.5);
		salarioBase<-40*precioHora;
		salario<-(40*precioHora)+(horasExtras*(precioHora*1.5));
	SiNo
		salario<-(horasTrabajadas*precioHora);
		salario<-salarioBase
	FinSi
	
	Escribir "reporte de salario con horas extras remuneradas" 
	Escribir "Señor@:",nombre
	Escribir "sus horas trabajadas fueron: ", horasTrabajadas
	Escribir "sus horas extras fueron: ",horasExtras
	Escribir "Su salario base fue: ", salarioBase
	Escribir "su salario con horas extras fue", salarioExtras
	Escribir "su salario total fue:", salario
	
	
	
FinAlgoritmo
