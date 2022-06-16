# Proyecto Programado
# Profesor: Berrocal Brenes Gonzalo Alberto
# Asignatura: Programacion Basica SC-115 / Grupo No. 5
# Programado por:
# Salas Solis Marco
# Calderon Najera Justin Andres
# Fernandez Delgado Michael Andrey
# Fajardo Cascante Saiden

# Importacion de Librerias
import os

# Declaracion de Variable

# Declaracion de Funciones
def menuLogueo():
    print("*****************************************************************")
    print("*           AGUAS TERMALES                                      *")
    print("*                         PARAISO AZUL                          *")
    print("*                                                               *")
    print("*  WELCOME / WILOMEN / BIENVENIDO / BIENVENUE / приветствовать  *")
    print("*                                                               *")
    print("*****************************************************************")
    print("*  ACCESSO SEGURO AL SISTEMA, SOLO USUARIOS REGISTRADOS         *")
    print("*                                                               *")
    print("*****************************************************************")




def menuPrincipal():
    opcion = 0
    while opcion != 4:
        print("*********************************************")
        print("*                                           *")
        print("*     Aguas Termales                        *")
        print("*     Paraiso Azul                          *")
        print("*     Bienvenidos!                          *")
        print("*                                           *")
        print("*********************************************")
        print("*                                           *")
        print("*  1. Registro.                             *")
        print("*  2. Ventas de Naturales.                  *")
        print("*  3. Historial.                            *")
        print("*  4. Salir:                                *")
        print("*                                           *")
        print("*********************************************")
        opcion = int(input("Escoja una  opcion: "))
        if opcion == 1:
            print("Modulo de Registro")
        elif opcion == 2:
            print("Modulo de Ventas")
        elif opcion == 3:
            print("Modulo Historial")
        elif opcion == 4:
            SystemExit()
        else:
            print("Error en la seleccion...intentelo de nuevo")


# ************************************
os.system('cls')
#menuPrincipal()
menuLogueo()
