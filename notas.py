def Solicitud():
    notas = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    for i in range (1,6):
        print(f"Estudiante #{i}")
        for x in range(1,4):
            nota = int(input(f"Ingrese la nota del curso #{x}: "))
            notas[i-1][x-1]= nota
    return notas

def PromedioGlobal(notas):
    promedio = 0
    for i in range(5):
        for x in range(3):
            promedio += notas[i][x]
    promedio = promedio / 15
    promedio = round(promedio,2)
    print("")
    print(f"El promedio de notas es de {promedio}")
    
def PromedioCur2(notas):
    curso2 = 1
    promedio = 0
    for i in range(5):
        promedio += notas[i][curso2]
    promedio = promedio / 5
    promedio = round(promedio,2)
    print(f"El promedio de notas de el curso #2 es de: {promedio}")

def MayorCurs3(notas):
    curso3 = 2
    mayor = 0
    for i in range(5):
        if notas[i][curso3] >= mayor:
            mayor = notas[i][curso3]

    print(f"La nota mas alta del tercer curso es: {mayor}")

def PromeEst5(notas):
    estudiante5 = 4
    promedio = 0
    for i in range(3):
        promedio += notas[estudiante5][i]
    promedio = promedio / 3
    promedio = round(promedio,2)
    print(f"El promedio de notas del estudiante #5 es de: {promedio}")
#programa principal--------
notas = Solicitud()
PromedioGlobal(notas)
PromedioCur2(notas)
MayorCurs3(notas)
PromeEst5(notas)
