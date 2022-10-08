'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 9: Repaso
Archivo Principal
Fecha: 18 De Octubre De 2022

La escuela campeones de la pizarra está teniendo problemas para la gestión de sus alumnos y calificaciones.
El director a solicitado la creación de un programa que permita obtener e imprimir el promedio grupal 
e individual de 10 estudiantes, los cuales pueden tener hasta 5 calificaciones.
Realiza el programa para solucionar el problema, contemplando las siguientes indicaciones:
    •    Utilizar una matriz para representar a los estudiantes y a las materias.
    •    Solicite al usuario la cantidad de materias (máximo 5, validar el dato).
    •    El usuario debe capturar las calificaciones.
    •    Se deberá obtener el promedio del grupo.
    •    Se deberá obtener el promedio por alumno.
    •    Se deberá obtener el alumno con el promedio más alto y el mas bajo.
    •    Se deberá hacer uso de funciones, un menú para elegir las opciones y validaciones en caso de ser necesario.
'''

from pract9Func import*

calif=capturaCalif()
listaPromedios=promedios(calif)
promMayor=califMayor(listaPromedios)
busquedaAlumno(listaPromedios,promMayor)
promMenor=califMenor(listaPromedios)
busquedaAlumno(listaPromedios,promMenor)
