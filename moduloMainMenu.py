def MainMenu(acceso):
    if acceso == 1:
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
        valores = [1,2,3,4]
        modulo = int(input())
        while not modulo in valores:
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
            modulo = int(input())


    return modulo

acceso = 1
MainMenu(acceso)
