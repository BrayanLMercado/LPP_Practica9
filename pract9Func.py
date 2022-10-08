'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 9: Repaso
Archivo De Funciones
Fecha: 18 De Octubre De 2022
'''

def capturaCalif():
    grupo=[]
    canMaterias=int(input("Cantidad De Materias (Max 5): "))
    while canMaterias<0 or canMaterias>5:
        print("Captura Una Cantidad Valida")
        canMaterias=int(input("Cantidad De Materias (Max 5): "))
    for x in range (10):
        print("Alumno:",x+1)
        grupo.append([])
        for t in range(canMaterias):
            print("Calificación:",t+1,end=" ")
            calif=float(input("Calificación Del Alumno: "))
            while calif<0 or calif>100:
                print("Captura Una Calificación Valida: (0 a 100) ")
                calif=float(input("Calificación Del Alumno: "))
            grupo[x].append(calif)
    print()
    return grupo
       
def promedios(matriz):
    sumaTotal=0
    materiasTotales=0
    promedios=[]
    for x in range(len(matriz)):
        sumaRenglon=0
        elementos=0
        for t in range(len(matriz[x])):
            sumaRenglon+=matriz[x][t]
            elementos+=1
        sumaTotal+=sumaRenglon
        materiasTotales+=elementos
        promedioRenglon=sumaRenglon/elementos
        promedios.append(promedioRenglon)
        print("El Promedio Del Alumno",x+1,"Es:",round(promedioRenglon,2))
    promedioMatrix=sumaTotal/materiasTotales
    print("El Promedio Del Grupo Es:",round(promedioMatrix,2)),print()
    return promedios

def califMenor(array):
    menor=array[0]
    for x in array:
        if x<menor:
            menor=x
    print("El Promedio Más Bajo Es",menor)
    return menor

def califMayor(array):
    mayor=array[0]
    for x in array:
        if x>mayor:
            mayor=x
    print("El Promedio Más Alto Es:",mayor)
    return mayor

def busquedaAlumno(array,prom):
    for x in range(len(array)):
        if array[x]==prom:
            print("El Promedio Lo Tiene El Alumno",x+1)
            print()
