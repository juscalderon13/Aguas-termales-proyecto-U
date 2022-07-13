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

SubModulCitas()
