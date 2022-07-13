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
SubModuloLisProduc()
