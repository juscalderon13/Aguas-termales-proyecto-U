#Entrada de variables Usuario y contraseña

user_1="admin"
pwd_1="123456"



#Saludo de ingreso a datos
print("Bienvenido ingrese su usuario y contraseña")

#proceso de transformacion, ingreso de datos
 

#usuario incorrecto
namUser=input("Digite su Usuario: \n")
if namUser !=user_1:
   print("Usuario incorrecto intente de nuevo")
   namUser=input("Digite su Usuario: \n")  

  
#contraseña incorrecta
pwdUser=input("Digite su contraseña: \n")
if pwdUser !=pwd_1:
 print("Contraseña incorrecta intente de nuevo")
 pwdUser=input("Digite su contraseña: \n")

if namUser==user_1 and pwdUser==pwd_1 :
   print("Usuario y contraseña valida")    
 
else:  
      print("2 intentos fallidos")
      print("No se puede ingresar al sistema")



            

