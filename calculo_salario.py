
# Ejercicio 1: Reescribe el programa del cálculo del salario para darle al empleado
# 1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.
# Introduzca las Horas: 45
# Introduzca la Tarifa por hora: 10
# Salario: 475.0

try:
	horas_work_totales = int(input ('introduzca las horas trabajadas: '))
	tarifa_horas = int(input ('introduzca la tarifa por horas: '))
	exceso_horas = 0


	if horas_work_totales < 40 : 
		exceso_horas = 0
		horas_work	 = horas_work_totales - exceso_horas
	else :	
		exceso_horas = horas_work_totales - 40 
		horas_work	 = horas_work_totales - exceso_horas



	salario = horas_work * tarifa_horas + exceso_horas * (tarifa_horas * 1.5)

	print ('El salario es: ',salario)

except:
	print ('introduca un número válido')

	


