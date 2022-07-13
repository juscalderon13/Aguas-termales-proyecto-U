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
