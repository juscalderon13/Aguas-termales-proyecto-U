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
""")
    #variable submodulo Historial para seleccionar opciones en modulo historial
    print("Desea ir al: ")
    subModHis = int(input())
    valores = [1,2,3]
    while not subModHis in valores:
        print("""
                 VALOR INVALIDO!
porfavor seleccione una de las siguientes opciones: """)
        print("""
[1] - Listado de aforo por día según el tipo de persona que ingreso.
[2] - citas programadas de acuerdo a los clientes registrados.
[3] - Listado de productos, segun articulos facturados.
""")
        print('Desea ir al:')
        subModHis = int(input())
    return subModHis
ModuloHistorial()
