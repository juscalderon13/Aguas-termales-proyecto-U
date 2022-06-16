#registro de visitantes

print("Bienvenido Dijite sus datos personales")
nombre=input("Nombre:")
apellido=input("Apellido:")
apellido2=input("2do apellido:")
cedula=int(input("Dijite su numero de cedula:"))
celular=int(input("Dijite su numero telefonico:"))
correo=input("Dijite su correo electronico:")
Direccion=input("dijite su direccion de domicilio:")
pais=int(input("Dijite 1 si es nacional o 2 si es extrangero:"))
if pais==1:
    print("Nacional")
elif pais==2:
    print("Extrangero")
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
fecha=int(input("Dijite la fecha en la desea reservar:"))
print("la fecha de reservacion es:",fecha)
turno=int(input("Dijite 1 para el turno de la mañana,2 para tarde y 3 para noche:"))
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

    
