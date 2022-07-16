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
