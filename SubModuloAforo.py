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
SubModulAforo()
