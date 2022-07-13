#Bienvenida y login
def Login():
    #Bienvenida
    print("-"*80)
    print('')
    print('              BIENVENIDO(A) A LAS AGUAS TERMALES PARAISO AZUL!')
    print('')

    # Login
    print("-"*80)
    print("-"*31, "INICIO DE SESION", "-"*31)
    print("-"*80)
    print('')
    print("Por favor Ingrese su nombre de usuario y contraseña para iniciar sesion.")
    print('')

    #Usuario y contraseña
    user = "admin"
    contra = "1234"

    #Solicitud de usuario y contraseña
    nomUser = input("Usuario: \n")
    contraUser = input("Contraseña: \n")
    acceso = 0

    #proceso de login
    #caso de usuario y contraseña incorrectas
    while user != nomUser or contra != contraUser :
        print(" "*13, "EL NOMBRE DE USUARIO Y CONTRASENA SON INCORRECTOS!")
        print("")
        nomUser = input("Usuario: \n")
        contraUser = input("Contraseña: \n")

    #login exitoso
        if user == nomUser and contra == contraUser :
            print("")
            print(" "*28, "INICIO DE SESION EXITOSO!")
            print("")
            print("-"*80)
            acceso = 1
        else:
            print(" "*27, "ERROR, INTENTE OTRA VEZ")
    return acceso

def MainMenu(acceso):
    if acceso == 1:
        print("-"*32, "MENU PRINCIPAL", "-"*32)
        print("-"*80)
        print('')
        print("""Bienvenido al menu principal ingrese el numero de una de las siguientes opciones:

[1] - Registro de Visitantes y Agendas de visita
[2] - Venta de productos
[3] - Historial
[4] - Salir
""")
    
#variable modulo para seleccionar los modulos del menu
        print("Desea ir al: ")
        valores = [1,2,3,4]
        modulo = int(input())
        while not modulo in valores:
            print("""
                 VALOR INVALIDO!
porfavor seleccione una de las siguientes opciones: """)
            print("""
[1] - Registro de Visitantes y Agendas de visita
[2] - Venta de productos
[3] - Historial
[4] - Salir
""")
            print("Desea ir al: ")
            modulo = int(input())


    return modulo

def ModuloRegisyAgen():
    print("")
    print("-"*80)
    print("-"*30, "REGISTROS Y AGENDAS", "-"*29)
    print("-"*80)
    print('')
    print("""Ingrese el numero del modulo al que desea ir:

[1] - Registro de visitantes
[2] - Agenda de visitas
""")
    print('Desea ir al:')
        
    #variable submodulo Registro para seleccionar opciones en el menu de Registro
    valores = [1,2]
    subModReg = int(input())
    while not subModReg in valores:
        print("""
                 VALOR INVALIDO!
porfavor seleccione una de las siguientes opciones: """)
        print("""
[1] - Registro de visitantes
[2] - Agenda de visitas
""")
        print('Desea ir al:')
        subModReg = int(input())
    return subModReg

acceso = Login()
modulo = MainMenu(acceso)


    
