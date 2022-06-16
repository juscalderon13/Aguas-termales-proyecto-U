#Intro al modulo
print("-"*80)
print("-"*35, "HISTORIAL", "-"*34)
print("-"*80)
print('')
        
#submenu de historial
print("""Digite el numero al que desea ir:

1 - Listado de aforo por día según el tipo de persona que ingreso.
2 - citas programadas de acuerdo a los clientes registrados.
3 - Listado de productos, segun articulos facturados.
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
    print()
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

1 - Volver al menu de Historial.
2 - Volver al menu principal. \n''')
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

1 - Volver al menu de Historial.
2 - Volver al menu principal. \n''')
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

1 - Volver al menu de Historial.
2 - Volver al menu principal. \n''')
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
