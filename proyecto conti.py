#registro de visitantes

print("Bienvenido Ingrese sus datos personales")
nombre = input("Nombre: ")
apellidos = input("Apellidos: ")
cedula = int(input("Digite su numero de cedula o pasaporte: "))
celular = int(input("Digite su numero telefonico: "))
correo = input("Digite su correo electronico: ")
Direccion = input("digite su direccion de domicilio: ")
pais=int(input("Digite 1 si es nacional o 2 si es extranjero: "))
if pais==1:
    print("Nacional")
elif pais==2:
    print("Extranjero")
else:
      print("no aplica")
edad=int(input("Dijite su edad:"))
if edad<18:
    print("NIÑO")
elif (edad>=18) and (edad<65):
    print("ADULTO")
elif edad>=65:
    print("ADULTO MAYOR")
#parte B
print("AGENDA DE VISITA")
fecha=int(input("Ingrese la fecha en la desea reservar (DD/MM/AAAA): "))
print("la fecha de reservacion es:",fecha)
Nombre= input('Ingrese el nombre del cliente: ')
turno=int(input("""seleccione:
1 - para el turno de la mañana.
2 - para elturno de la tarde.
3 -  para el turno de la noche. """))
if turno==1:
          print("turno de la mañana")
if turno==2:
          print("turno de la tarde")
if turno==3:
          print("turno de la noche")
else:
          print("no aplica")
reservador=input("Dijite el nombre de la persona encargada de la reserva:")
print("El encargado de la reserva es:",reservador)
import random
print("Su numero de reservación es:",random.randint(100, 10000)) 

    
