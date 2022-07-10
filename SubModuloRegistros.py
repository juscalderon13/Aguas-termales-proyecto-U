def SubmodRegisVisit():
    print("")
    print("-"*80)
    print("-"*28, "REGISTRO DE VISITANTES", "-"*28)
    print("-"*80)
    print('')
    print("Ingrese los datos personales del cliente.")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    pais = int(input("Ingrese (1) si es nacional o (2) si es extranjero:"))
    if pais == 1:
        pais = "Nacional"
        Id_or_Pass = int(input("Numero de cedula: "))
    elif pais==2:
        pais ="Extranjero"
        Id_or_Pass = int(input("Numero de pasaporte: "))
    else:
        print("categoria invalida")
    celular = int(input("Numero telefonico: "))
    correo = input("Correo electronico: ")
    edad = int(input("Edad:"))
    categoria = 0
    if edad<18:
        categoria = "NIÑO"
    elif (edad>=18) and (edad<65):
        categoria = "ADULTO"
    elif edad>=65:
        categoria = "ADULTO MAYOR"
    print("")
    print(" "*30, "REGISTRO EXITOSO!")
    print(f"""Datos del registro
Nombre completo: {nombre} {apellidos}
Tipo de cliente: {pais}
Edad:            {edad}
categoria:       {categoria}
Celular:         {celular}
Correo:          {correo}""")
    print("")
    print('''Digite el numero al que desea ir:

[1] - Realizar un nuevo registro.
[2] - Volver al menu de registros y agendas.
[3] - Volver al menu principal.\n''')
    print('Desea ir al:')
    subModRegistro = int(input())
    valores = [1,2,3]
    while not subModRegistro in valores:
        print("""
                 VALOR INVALIDO!
porfavor seleccione una de las siguientes opciones: """)
        print("""
[1] - Realizar un nuevo registro.
[2] - Volver al menu de registros y agendas.
[3] - Volver al menu principal.
""")
        print('Desea ir al:')
        subModRegistro = int(input())
    return subModRegistro

SubmodRegisVisit()
