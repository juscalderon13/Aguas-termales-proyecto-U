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
            acceso = 1
    return acceso

def MainMenu():
    print("-"*80)
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

[1] - Realizar otra reservacion.
[2] - Volver al menu de Registros y Agendas.\n''')
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

def ModuloVentas():
    print("")
    print("-"*80)
    print("-"*36, "VENTAS", "-"*36)
    print("-"*80)
    print('')
    nombre = input("Ingresa el nombre del cliente para la factura: ")
    cafe = 1500
    llavero = 1000
    gorra = 5000
    chocolate = 2500
    iva = 0.13
    descuento = 10

    #Mostrar menú disponible para compras.
    print("\nElige el producto que deseas comprar")
    print("""
[1] = Café nacional
[2] = Llavero típico
[3] = Gorra con mensaje nacional
[4] = Chocolate de café nacional""")

    #Operaciones.


    #Se selecciona los productos deseados.
    eleccion = input("\nSelecciona el producto que desees: ")
    if eleccion == "1":
        print("Has seleccionado Café nacional")
        cantidad = int(input("Cantidad de paquetes: "))
        total = print("\nEl total sería: ", cantidad * cafe, "colones")
    elif eleccion == "2":
        print("Has seleccionado Llavero típico")
        cantidad = int(input("Cantidad de llaveros: "))
        total2 = print("\nEl total sería: ", cantidad * llavero, "colones")
    elif eleccion == "3":
        print("Has seleccionado Gorras con mensaje nacional")
        cantidad = int(input("Cantidad de gorras: "))
        total3 = print("\nEl total sería: ", cantidad * gorra, "colones")
    elif eleccion == "4":
        print("Has seleccionado Chocolates de café nacional")
        cantidad = int(input("Cantidad de chocolates: "))
        total = print("\nEl total sería: ", cantidad * chocolate, "colones")
    else:
        print("Opción inexistente, elige una opción válida")
    
    #Factura final
    print("\nFactura a nombre de: ", nombre)
    print("Los productos que lleva son: ")
    print("El precio total es: ")
    print("El IVA correspondiente es del 13%")
    print("El precio de los productos con el IVA es de: ")
    print("El descuento a aplicar es de: ", descuento, "%")
    print("El precio total con el descuento es: ")
    print("El precio final de los productos seria: ")
    print('')
    print('''Ingrese el numero al que desea ir:

[1] - Realizar otra venta.
[2] - Volver al menu principal. \n''')
    print('Desea ir al:')
    subModVentas = int(input())
    valores = [1,2]
    while not subModVentas in valores:
        print("""
                 VALOR INVALIDO!
porfavor seleccione una de las siguientes opciones: """)
        print("""
[1] - Realizar otra venta.
[2] - Volver al menu principal.
""")
        print('Desea ir al:')
        subModVentas = int(input())
    return subModVentas

def ModuloHistorial():
    print("")
    print("-"*80)
    print("-"*35, "HISTORIAL", "-"*34)
    print("-"*80)
    print('')
    print("""Ingrese el numero del modulo al que desea ir:

[1] - Listado de aforo por día según el tipo de persona que ingreso.
[2] - citas programadas de acuerdo a los clientes registrados.
[3] - Listado de productos, segun articulos facturados.
[4] - Volver al Menu Principal.
""")
    #variable submodulo Historial para seleccionar opciones en modulo historial
    print("Desea ir al: ")
    subModHis = int(input())
    valores = [1,2,3,4]
    while not subModHis in valores:
        print("""
                 VALOR INVALIDO!
porfavor seleccione una de las siguientes opciones: """)
        print("""
[1] - Listado de aforo por día según el tipo de persona que ingreso.
[2] - citas programadas de acuerdo a los clientes registrados.
[3] - Listado de productos, segun articulos facturados.
[4] - Volver al Menu Principal.
""")
        print('Desea ir al:')
        subModHis = int(input())
    return subModHis

def SubModulAforo():
    nino = 2
    adulto = 9
    adultoMa = 15
    #total de aforo por dia
    totalAfor = nino + adulto + adultoMa
    #Nombre de persona
    name = "Elvis Tec"
    #fecha valida por el momento
    fecha = "15/06/2022"
    hora = '12:30 p.m.'
    numeroReser = "#3246"
    estado = "Pago"
    print("")
    print("-"*80)
    print("-"*32, "LISTA DE AFORO", "-"*32)
    print("-"*80)
    print('')
    print("Ingrese la fecha que desea ver el historial en el siguiente formato \n (DD/MM/AAAA): \n")
    fechaInp = input()
    if fecha != fechaInp:
        print('fecha invalida por favor intente de nuevo')
    else:
        print(" "*20,f"Historial del dia {fechaInp}. \n")
        print(f'El aforo fue de {totalAfor} personas entre los siguientes tipos: \n')
        print(f'niños: {nino}')
        print(f'Adultos: {adulto}')
        print(f'Adultos mayores: {adultoMa}')
        enter = input()
        print('')
        print('''Digite el numero al que desea ir:

[1] - Volver al menu de Historial.
[2] - Volver al menu principal. \n''')
        print('Desea ir al:')
        subModAforo = int(input())
        valores = [1,2]
        while not subModAforo in valores:
            print("""
                 VALOR INVALIDO!
porfavor seleccione una de las siguientes opciones: """)
            print("""
[1] - Volver al menu de Historial.
[2] - Volver al menu principal.
""")
            print('Desea ir al:')
            subModAforo = int(input())
    return subModAforo

def SubModulCitas():
    nino = 2
    adulto = 9
    adultoMa = 15
    #total de aforo por dia
    totalAfor = nino + adulto + adultoMa
    #Nombre de persona
    name = "Elvis Tec"
    #fecha valida por el momento
    fecha = "15/06/2022"
    hora = '12:30 p.m.'
    numeroReser = "#3246"
    estado = "Pago"
    print("")
    print("-"*80)
    print("-"*30, "CITAS PROGRAMADAS", "-"*31)
    print("-"*80)
    print('')
    print('Ingrese la fecha para ver las reservaciones de ese dia \n (DD/MM/AAAA): \n')
    fechaInp = input()
    if fecha != fechaInp:
        print('fecha invalida por favor intente de nuevo')
    else:
        print(" "*20,f"Reservaciones del dia {fechaInp}. \n")
        print(f'[Reservacion]         [nombre]          [Hora]        [Estado]')
        print(f" {numeroReser}                 {name}        {hora}     {estado}")
        print('')
        enter = input("Presione ENTER para continuar")
        print('''Digite el numero al que desea ir:

[1] - Volver al menu de Historial.
[2] - Volver al menu principal. \n''')
        print('Desea ir al:')
        subModCitas = int(input())
        valores = [1,2]
        while not subModCitas in valores:
            print("""
                 VALOR INVALIDO!
porfavor seleccione una de las siguientes opciones: """)
            print("""
[1] - Volver al menu de Historial.
[2] - Volver al menu principal.
""")
            print('Desea ir al:')
            subModCitas = int(input())
    return subModCitas

def SubModuloLisProduc():
    print("")
    print("-"*80)
    print("-"*30, "LISTA DE PRODUCTOS", "-"*30)
    print("-"*80)
    print('')
    print('[Producto]        [Vendidos]       [stock]        [Precio de venta]')
    print(" Crema facial         7              12                  $45")
    print(' Crema humectante     4              15                  $35')
    print('')
    print('''Digite el numero al que desea ir:

[1] - Volver al menu de Historial.
[2] - Volver al menu principal. \n''')
    print('Desea ir al:')
    subModLista = int(input())
    valores = [1,2]
    while not subModLista in valores:
            print("""
                 VALOR INVALIDO!
porfavor seleccione una de las siguientes opciones: """)
            print("""
[1] - Volver al menu de Historial.
[2] - Volver al menu principal.
""")
            print('Desea ir al:')
            subModLista = int(input())
    return subModLista

def ModuloExit():
    print("")
    print("-"*80)
    print("-"*36, "SALIR", "-"*37)
    print("-"*80)
    print('')
    print('Esta saliendo de la aplicacion digite: ')
    print("""
[1] - Para salir de la aplicacion y cerrar sesion. 
[2] - Cancelar y volver al menu principal
""")
    #variable submodulo salida para seleccionar opciones en modulo salida
    print('Desea cerrar sesion? :')
    subModSalir = int(input())
    valores = [1,2]
    while not subModSalir in valores:
        print("""
                 VALOR INVALIDO!
porfavor seleccione una de las siguientes opciones: """)
        print("""
[1] - Para salir de la aplicacion y cerrar sesion. 
[2] - Cancelar y volver al menu principal
""")
        print('Desea ir al:')
        subModSalir = int(input())
    return subModSalir

#Modulo de verificacion de usuario, si usuario es verificado acceso = 1
acceso = Login()
while acceso == 1: #Bucle para tener el Menu siempre abierto hasta que se desee salir
    moduloPrincipal = MainMenu() #Modulo de menu principal para seleccionar al modulo que se desea ir
    #CASO PARA ENTRAR EN EL MODULO DE REGISTROS
    if moduloPrincipal == 1: #Si modulo menu principal es igual a 1
        while moduloPrincipal == 1: #Bucle para mantener activo este modulo hasta que se desee salir
            x = ModuloRegisyAgen() #Solicitud de correr este modulo siempre que sea igual a 1
            if x == 1:  #si modulo de registros es igual a 1 va a Registro de visitas
                y = SubmodRegisVisit() #se activa modulo de registro de visitas
                while y == 1: #se utiliza un bucle para mantenerlo activo hasta que se desee salir
                    y = SubmodRegisVisit() #se activa modulo registro de visitas en el bucle
            elif x == 2: #si modulo registros es igual a 2 va a modulo agenda de visitas
                z = SubModulAgenVisit() #se activa modulo de agenda de visitas
                while z == 1: # se utiliza un bucle para mantenerlo activo lo que se desee
                    z = SubModulAgenVisit() #se activa modulo de agenda de visitas dentro del bucle
            else: #caso en el que se selecciona el 3 en el modulo de Registros y ventas que genera el regreso al menu principal
                moduloPrincipal = 0 #se pone el modulo en 0 para cerrar el Modulo de Registros y agenda
    #CASO PARA ENTRAR EN EL MODULO DE VENTAS
    elif moduloPrincipal == 2: #si modulo menu principal es igual a 2
        while moduloPrincipal == 2: #Bucle para mantener este modulo activo lo que se le solicite
            x1 = ModuloVentas() #activacion del modulo de ventas
            if x1 == 2: #si modulo Ventas es igual a 2 se cierra el modulo de ventas
                moduloPrincipal = 0 #solicitamos que el modulo principal sea igual a 0 para cerrar el modulo de ventas
    #CASO PARA ENTRAR EN EL MODULO DE HISTORIAL
    elif moduloPrincipal == 3: #si modulo menu principal es igual a 3
        while moduloPrincipal == 3: #se crea un modulo de menu principal
            x2 = ModuloHistorial() #activacion del modulo de historial
            if x2 == 1: #si modulo hsitorial retorna 1
                y2 = SubModulAforo() #se activa modulo de aforo diario
                while y == 1: #bucle para mantener activo el modulo de aforo el tiempo necesario
                    y2 = SubModulAforo() #activacion de modulo aforo dentro del bucle en caso de necesitar utlizarlo otra vez
            elif x2 == 2: #si modulo historial retorna 2
                z2 = SubModulCitas() #activacion del modulo de citas reservadas
                while z2 == 2: #bucle para mantener activo el modulo de citas el tiempo necesario
                    z2 = SubModulCitas() #activacion del modulo de citas reservadas dentro del bucle en caso de utilizarlo otra vez
            elif x2 == 3: #si modulo historial es igual a 3
                a2 = SubModuloLisProduc() #activacion del modulo de lista de productos
                while a2 == 3: #Bucle para mantener activo el modulo lo que sea necesario
                    a2 = SubModuloLisProduc() #Activacion del modulo de listas dentro del bucle en caso de utlizarlo mas veces
            else: #si modulo historial es igual a 4
                moduloPrincipal = 0 #el modulo principal va a ser igual a 0 para regresar al menu principal
    #CASO PARA ENTRAR EN EL MODULO DE SALIDA
    elif moduloPrincipal == 4: #si modulo principal es igual a 4
        salida = ModuloExit() #activacion del modulo de salida
        if salida == 1: #si confirma la salida retorna 1
            acceso = 0 #entonces acceso pasa a ser 0 cerrando la aplicacion
