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
            print("-"*32, "MENU PRINCIPAL", "-"*32)
            print("-"*80)
            print('')
            return 1
            break
        else:
            print(" "*27, "ERROR, INTENTE OTRA VEZ")
    

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

def SubmodRegisVisit():
    print("")
    print("-"*80)
    print("-"*28, "REGISTRO DE VISITANTES", "-"*28)
    print("-"*80)
    print('')
    print("Ingrese los datos personales del cliente.")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
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


