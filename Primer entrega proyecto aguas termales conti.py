# Proyecto Aguas termales
# Profesor: Berrocal Brenes Gonzalo Alberto
# Asignatura: Programacion Basica SC-115 / Grupo No. 5
# Equipo: Conti Fidelitas
# Programado por:
# Salas Solis Marco
# Calderon Najera Justin Andres
# Fernandez Delgado Michael Andrey
# Fajardo Cascante Saiden

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
#caso de usuario incorrecto
if user != nomUser and contra == contraUser :
    print(" "*20, "EL NOMBRE DE USUARIO ES INCORRECTO!")
    
#caso de contraseña incorrecta
elif user == nomUser and contra != contraUser :
    print(" "*22, "LA CONTRASENA ES INCORRECTA!")
    
#caso de usuario y contraseña incorrectas
elif user != nomUser and contra != contraUser :
    print(" "*13, "EL NOMBRE DE USUARIO Y CONTRASENA SON INCORRECTOS!")
    
#login exitoso
elif user == nomUser and contra == contraUser :
    print("")
    print(" "*28, "INICIO DE SESION EXITOSO!")
    print("")
    print("-"*80)
    print("-"*32, "MENU PRINCIPAL", "-"*32)
    print("-"*80)
    print('')
    
#menu principal
    print("""Bienvenido al menu principal ingrese el numero de una de las siguientes opciones:

[1] - Registro de Visitantes y Agendas de visita
[2] - Venta de productos
[3] - Historial
[4] - Salir
""")
    
#variable modulo para seleccionar los modulos del menu
    print("Desea ir al: ")
    modulo = int(input())
    
    #caso de entrada al modulo de registro y agendas
    if modulo == 1 :
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
        subModReg = int(input())
        
        #caso de entrada a registro de visitantes
        if subModReg == 1 :
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
            if subModRegistro == 1:
                print("Realizara un nuevo registro")
            elif subModRegistro == 2:
                print('Volvera al menu de Registros y menu')
            elif subModRegistro == 3:
                print('Volvera al menu principal')
            else:
                print('Valor invalido intente de nuevo')
            
            
        #caso de entrada a agenda de visitas
        elif subModReg == 2 :
            print("")
            print("-"*80)
            print("-"*30, "AGENDA DE VISITAS", "-"*31)
            print("-"*80)
            print('')
            fecha=input("Ingrese la fecha en la desea reservar (DD/MM/AAAA): ")
            print("la fecha de reservacion es:",fecha)
            Nombre= input('Ingrese el nombre del cliente: ')
            turno=int(input("""seleccione:

[1] - para el turno de la mañana.
[2] - para el turno de la tarde.
[3] - para el turno de la noche.

Desea ir al:
"""))
            print("")
            print("Usted selecciono: ")
            if turno == 1:
                print("turno de la mañana")
            if turno==2:
                print("turno de la tarde")
            if turno==3:
                print("turno de la noche")
            else:
                print("no aplica")
            reservador=input("Ingrese el nombre de la persona encargada de la reserva:")
            print("El encargado de la reserva es:",reservador)
            import random
            print("Su numero de reservación es:",random.randint(100, 10000))

            print('''Ingrese el numero al que desea ir:

[1] - Volver al menu de registros y agendas.
[2] - Volver al menu principal.\n''')
            print('Desea ir al:')
            subModAgenda = int(input())
            if subModAgenda == 1:
                print('Volvera al menu de Registros y menu')
            elif subModAgenda == 2:
                print('Volvera al menu principal')
            else:
                print('Valor invalido intente de nuevo')
        #caso de error por valor incorrecto
        else:
            print(" "*27, "EL VALOR ES INVALIDO!")
            
    #caso de entrada al modulo de ventas
    elif modulo == 2:
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
        if subModVentas == 1:
            print("Realizara otra venta")
        elif subModVentas == 2:
            print('Volvera al menu principal')
        else:
            print('Valor invalido intente de nuevo')
            
    #caso de entrada al modulo de historial
    elif modulo == 3 :
        print("")
        print("-"*80)
        print("-"*35, "HISTORIAL", "-"*34)
        print("-"*80)
        print('')
        print("""Ingrese el numero del modulo al que desea ir:

[1] - Listado de aforo por día según el tipo de persona que ingreso.
[2] - citas programadas de acuerdo a los clientes registrados.
[3] - Listado de productos, segun articulos facturados.
""")
        #variable submodulo Historial para seleccionar opciones en modulo historial
        print("Desea ir al: ")
        subModHis = int(input())
        #tipos de personas
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

        #caso de entrada a listado de aforo
        if subModHis == 1:
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
                print('')
                print('''Digite el numero al que desea ir:

[1] - Volver al menu de Historial.
[2] - Volver al menu principal. \n''')
                print('Desea ir al:')
                subModAforo = int(input())
                if subModAforo == 1:
                    print("volvera al menu Historial")
                elif subModAforo == 2:
                    print('Volvera al menu principal')
                else:
                    print('Valor invalido intente de nuevo')

        #caso de entrada a citas programadas
        elif subModHis == 2 :
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
                print('''Digite el numero al que desea ir:

[1] - Volver al menu de Historial.
[2] - Volver al menu principal. \n''')
                print('Desea ir al:')
                subModCitas = int(input())
                if subModCitas == 1:
                    print("volvera al menu Historial")
                elif subModCitas == 2:
                    print('Volvera al menu principal')
                else:
                    print('Valor invalido intente de nuevo')

        #caso de entrada a lista de productos
        elif subModHis == 3 :
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
            if subModLista == 1:
                print("volvera al menu Historial")
            elif subModLista == 2:
                print('Volvera al menu principal')
            else:
                print('Valor invalido intente de nuevo')
        #caso de error
        else:
            print(" "*27, "EL VALOR ES INVALIDO!")
            
    #caso de salida de aplicacion
    elif modulo == 4 :
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
        
        #caso de cerrar sesion
        if subModSalir == 1 :
            print("")
            print("-"*80)
            print("-"*31, "SESION CERRADA", "-"*33)
            print("-"*31, " HASTA PRONTO ", "-"*33)
            print("-"*80)
            print('')
        elif subModSalir == 2 :
            #algun dia esto volvera al menu pero por el momento
            print('Todavia estamos trabajando en eso.')
        else:
            print(" "*27, "EL VALOR ES INVALIDO!")
    else:
        print(" "*27,"EL VALOR ES INVALIDO!")
