#!/usr/bin/env python
#-*- coding: utf-8 -*-

from math import *
from sympy import *



print '\n\t\t:::: calculadora-cientifica by Kamaher ::::::::'
print '\n\t\t|||||||Calculadora escrita en Python |||||||||||'
opcion = input("\nElije opcion\n\t1.- Suma\t\t\t2.- Resta\n\t3.- Multiplicacion\t\t4.- Division con resto\n\t5.- Potencia\t\t\t6.- Cuadraticas\n\t7.- Seno\t\t\t8.- Coseno\n\t9.- Tangente\t\t\t10.-Raiz Cuadrada\n\t11.-Derivadas polinomica\t12.-Funcion exponencial\n\t13.-Limite\t\t\t14.-Integracion Definida\n\t15.-Salir \n\n Introduzca el valor de la opcion >>> ")
if (opcion == 1):
	
	#suma
	
	primer_numero = input("\nIntroduce el numero1 > ")
	segundo_numero = input("\nIntroduce el numero2 > ")
	resultado = primer_numero + segundo_numero
	print "\nEl resultado es :",resultado
	print '\n\n'
	
elif (opcion == 2):
	
	#resta
	
	numero1 = input("\nIntroduce el numero1 > ")
	numero2 = input("\nIntroduce el numero2 > ")
	resultado = numero1 - numero2
	print "\nEl resultado es :",resultado
	print '\n\n'
elif (opcion == 3):
	
	#multiplicación
	
	numero1 = input("\nIntroduce el numero1 > ")
	numero2 = input("\nIntroduce el numero2 > ")
	resultado = numero1 * numero2
	print "El resultado es :",resultado
	print '\n\n'
elif (opcion == 4):
	
	#división
	
	numero1 = input("\nIntroduce el numero1: ")
	numero2 = input("\nIntroduce el numero2: ")
	if (numero1 == 0):
		print '\nNo válido'
		print '\n\n'
	else:
		resultado = numero1 / numero2
		resto = numero1 % numero2
		print "El resultado es :",resultado
		print '\nEl resto es: '
		print resto
		print '\n\n'
		
elif (opcion == 5):
	
	#potencia
	
	numero1 = input("\nIntroduce el numero1 > ")
	numero2 = input("\nIntroduce el numero2 > ")
	resultado=numero1**numero2
	print '\nEl numero es: '
	print numero1
	print 'Y está elevado a: '
	print numero2
	print ("El resultado es: " , resultado)
	print '\n\n'
	
elif(opcion==6):
	
	#cuadratica
	
	def raiz(a,b,c):
		x1=(-b+(b**b-4*a*c)^(1/2))/(2*a)
		x2=(-b-(b**b-4*a*c)^(1/2))/(2*a)
		return x1, x2
	
	def main():
		d=int(input("A: "))
		e=int(input("B: "))
		f=int(input("C: "))
		resultado1,resultado2 =raiz(d,e,f)
		print "primera raiz :" ,resultado1,
		print "segunda raiz :" ,resultado2
	main()
elif(opcion==7):
	
	#seno
	
	q=float(raw_input("\n\tingrese el valor de X :"))
	seno=sin(q)
	print '\nEl Resultado es :',seno
	
elif(opcion==8):
	
	#coseno
	
	u=float(raw_input("\n\tingrese el valor de X :"))
	coseno=cos(u)
	print '\nEl Resultado es :',coseno
	
elif(opcion==9):
	
	#Tangente		
	
	t=float(raw_input("\n\tingrese el valor de X :"))
	tangente=tan(t)
	print '\nEl Resultado es :',tangente
	
	
elif(opcion==10):
	
	#raiz cuadrada
	
	c=float(raw_input("\nIngrese el valor que esta dentro de la raiz :"))
	raiz_cuadrada= sqrt(c)
	print '\nEl Resultado es :',raiz_cuadrada
	

elif(opcion==11):
	
	#Derivada polinomica

	x = Symbol('x')
	y = Symbol('y')
	z = Symbol('z')
 
	print "Introduce el polinomio: "
	derivada = input( );
	print "El polinomio derivado es: ", derivada
 
	# Se calculan las derivadas.
	print "La polinomio derivado, respecto a x: ", diff(f, x)
	print "El polinomio derivado, respecto a y: ", diff(f, y)
	
	
elif(opcion==12):
	
	#funcion exponencial
	
	b=int(raw_input("\nIngrese el valor X de e^x :"))
	exponencial=e**(b)
	print '\nResultado es :',exponencial
	
elif(opcion==13):
	
	#limite

	x=Symbol("x")
	o=int(raw_input("\nIntrodusca el valor de cuando x tiende a  :"))
	f=str(raw_input("\nIntrodusca la funcion :"))
	limite=limit(f,x,o)
	print '\nResultado es :',limite
	
elif(opcion==14):
	
	#integracion definida
	
	x, y = symbols('x,y')
	func =str(raw_input("\nIntroduce la funcion a integrar :"))
	lim1=float(raw_input("\nIntroduce el limite inferior de integracion :"))
	lim2=float(raw_input("\nIntroduce el limite superior de integracion :"))
	integral=integrate(func,(x,lim1,lim2) )
	print '\nResultado es :',integral
	
elif(opcion==15):
	
	#Salir
	
	print"\n\tGracias por usar mi pequena calculadora"
	print"\nSi desea salir presione enter"
	print"\n\n"
	exit()	

		
else:
	print 'No válido'
	print '\n\n\n'
print '\n\n\t\tRedondeandoainfinito.blogspot.com.ar'
print '\n\n'