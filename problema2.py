'''
	problema2.py
	Autor: juanyanza11
'''
x= input("Ingrese la variable x:\n")
y= input("Ingrese la variable y:\n")
z= input("Ingrese la variable z:\n")

#TRANSFORMAR STRING A FLOAT
numx= float(x)
numy= float(y)
numz= float(z)

# CALCULO DE m

m = (numx +(numy/numz))/(numx-(numy/numz))

# Muestra de datos en pantalla
print("\nEl valor de m, en base a las variables:\n x=%.1f\n\t y= %.1f\n\t\t z=%.1f\n da como resultado:\n\t\t\t m= %.1f\n"%(numx,numy,numz,m))