#Programa aprobar curso
import os

#Declaracion de variables
alumno,curso,nota1,nota2,nota3,promedio="","",0.0,0.0,0.0,0.0

#INPUT via OS
alumno=input ("Ingrese el alumno:")
curso=input ("Ingrese el curso:")
nota1=float(input("Ingrese nota1"))
nota2=float(input("Ingrese nota2"))
nota3=float(input("Ingrese nota3"))

#PROCESING
promedio= int(round((nota1+nota2+nota3)/3,0))

#Condicion multiple
# Si el prom => 55 y 60 (felicidades)
if ( promedio >=55 and promedio <=60 ):
    print("felicidades")
# Si el prom 50 y 54 (sigue asi)
if ( promedio >= 50 and promedio <= 54):
    print("sigue asi")

