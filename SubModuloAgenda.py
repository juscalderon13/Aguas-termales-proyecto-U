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

SubModulAgenVisit()
