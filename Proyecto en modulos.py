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
            
    if user == nomUser and contra == contraUser :
            print("")
            print(" "*28, "INICIO DE SESION EXITOSO!")
            print("")
            print("-"*80)
            acceso = 1
    return acceso

def MainMenu():
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
    valores = ["1","2","3","4"]
    seleccion = (input())
    while not seleccion in valores :
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
        seleccion = (input())
    modulo = int(seleccion)

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
[3] - Volver al menu principal
""")
    print('Desea ir al:')
        
    #variable submodulo Registro para seleccionar opciones en el menu de Registro
    valores = [1,2,3]
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

def SubmodRegisVisit():
    print("")
    print("-"*80)
    print("-"*28, "REGISTRO DE VISITANTES", "-"*28)
    print("-"*80)
    print('')
    print("Ingrese los datos personales del cliente.")
    nombre = input("Nombre: ")
    while nombre == "":
        print("")
        print("Este dato es obligatorio")
        print("   Ingrese otra vez")
        print("")
        nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    while apellidos == "":
        print("")
        print("Este dato es obligatorio")
        print("   Ingrese otra vez")
        print("")
        apellidos = input("Apellidos: ")
    pais = int(input("Ingrese (1) si es nacional o (2) si es extranjero:"))
    tipPais = [1,2]
    while not pais in tipPais:
        pais = int(input("Ingrese (1) si es nacional o (2) si es extranjero:"))
    if pais == 1:
        pais = "Nacional"
        Id_or_Pass = int(input("Numero de cedula: "))
    elif pais==2:
        pais ="Extranjero"
        Id_or_Pass = int(input("Numero de pasaporte: "))
    else:
        print("categoria invalida")
    celular = int(input("Numero telefonico: "))
    correo = input("Correo electronico: ")
    edad = int(input("Edad:"))
    categoria = 0
    if edad<18:
        categoria = "NIÑO"
    elif (edad>=18) and (edad<65):
        categoria = "ADULTO"
    elif edad>=65:
        categoria = "ADULTO MAYOR"
    print("")
    print(" "*30, "REGISTRO EXITOSO!")
    print(f"""Datos del registro
Nombre completo: {nombre} {apellidos}
Tipo de cliente: {pais}
Edad:            {edad}
categoria:       {categoria}
Celular:         {celular}
Correo:          {correo}""")
    print("")
    print('''Digite el numero al que desea ir:

[1] - Realizar un nuevo registro.
[2] - Volver al menu de registros y agendas.
[3] - Volver al menu principal.\n''')
    print('Desea ir al:')
    subModRegistro = int(input())
    valores = [1,2,3]
    while not subModRegistro in valores:
        print("""
                 VALOR INVALIDO!
porfavor seleccione una de las siguientes opciones: """)
        print("""
[1] - Realizar un nuevo registro.
[2] - Volver al menu de registros y agendas.
[3] - Volver al menu principal.
""")
        print('Desea ir al:')
        subModRegistro = int(input())
    return subModRegistro

def SubModulAgenVisit():
    import random

    print("")
    print("-"*80)
    print("-"*30, "AGENDA DE VISITAS", "-"*31)
    print("-"*80)
    print('')
    fecha = input("Ingrese la fecha en la desea reservar (DD/MM/AAAA): \n")
    print("la fecha de reservacion es:",fecha)
    Nombre = input('Ingrese el nombre del cliente: \n')
    turno = int(input("""seleccione:

[1] - para el turno de la mañana.
[2] - para el turno de la tarde.
[3] - para el turno de la noche.

Desea ir al:
"""))
    turnos = [1,2,3]
    while not turno in turnos:
        print("""
                 VALOR INVALIDO!
porfavor seleccione una de las siguientes opciones: """)
        print("""
[1] - para el turno de la mañana.
[2] - para el turno de la tarde.
[3] - para el turno de la noche.
""")
        print('Desea ir al:')
        turno = int(input())
        
    print("")
    print("Usted selecciono: ")
    if turno == 1:
        print("turno de la mañana")
    elif turno == 2:
        print("turno de la tarde")
    elif turno == 3:
        print("turno de la noche")
    else:
        print("no aplica")
    reservador = input("Ingrese el nombre de la persona encargada de la reserva:")
    print("El encargado de la reserva es:",reservador)
    print("Su numero de reservación es:",random.randint(100, 10000))

    print('''Ingrese el numero al que desea ir:

[1] - Volver al menu de registros y agendas.
[2] - Volver al menu principal.\n''')
    print('Desea ir al:')
    subModAgenda = int(input())
    valores = [1,2]
    while not subModAgenda in valores:
         print("""
                 VALOR INVALIDO!
porfavor seleccione una de las siguientes opciones: """)
         print("""
[1] - Volver al menu de registros y agendas.
[2] - Volver al menu principal.
""")
         print('Desea ir al:')
         subModAgenda = int(input())
    return subModAgenda

acceso = Login()
while acceso == 1:
    moduloPrincipal = MainMenu()
    if moduloPrincipal == 1:
        while moduloPrincipal == 1:
            x = ModuloRegisyAgen()
            if x == 1:
                y = SubmodRegisVisit()
                while y == 1:
                    y = SubmodRegisVisit()
            elif x == 2:
                z = SubModulAgenVisit()
                while z == 1:
                    z = SubModulAgenVisit()
                    
            
