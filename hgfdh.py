def ModuloVentas():
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

ModuloVentas()
