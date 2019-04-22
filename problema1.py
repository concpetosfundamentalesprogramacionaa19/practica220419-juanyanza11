''' 
	Problema 1
	Autor: juanyanza11
'''


numeroH =input("Ingrese el número de horas:\n")
costoH =input("Ingrese el costo por hora:\n")

# CÁLCULO DE DESCUENTO Y SUELDO
sueldo= float(numeroH) * float(costoH) 
descuentoS= 0.10 * float(sueldo)
sueldof= sueldo - 0.10 * sueldo

print("Su sueldo en base a horas es: %.2f \nCon un descuento del 10 por ciento: %.2f \nSu sueldo a pagar es: %.2f" %(sueldo, descuentoS, sueldof))
