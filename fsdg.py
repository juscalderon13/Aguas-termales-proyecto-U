login = {"marco":"123","justin":"124"}

solicitud = input("Digite usuario:")
contra = login[solicitud]
contador = 0

while contador <= 3:
    
    if solicitud in login:
        valor = 1  

    else:
        valor = 0

    contrasena = input("Digite contraseña:")

    if contra == contrasena:
        print("login exitoso")

    else:
        contador += 1
        print("Contraseña incorrecta")
