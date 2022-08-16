mediciones = []
print("Ingrese 'a' para voltajes altos y 'b' para voltajes bajos")
print("para voltajes erroreneos ingrese cualquier otro valor")
for i in range (1,11):
    medicion = input(f"Ingrese la medicion #{i}: ")
    mediciones.append(medicion)

voltAlto = mediciones.count("a")
voltBajo = mediciones.count("b")
voltErro = len(mediciones) - voltAlto - voltBajo

print(f"\n La cantidad de lecturas altas fue de: {voltAlto}")
print(f"La cantidad de lecturas Bajas fue de: {voltBajo}")
print(f"La cantidad de lecturas erroneas fue de: {voltErro}")

file = open("voltajes.txt","a")
file.write("Lecturas altas: ")
file.write(str(voltAlto))
file.write("\n")
file.write("Lecturas Bajas: ")
file.write(str(voltBajo))
file.write("\n")
file.write("Lecturas erroneas: ")
file.write(str(voltErro))
file.write("\n")
file.close()

for i in range(10):
    mediciones[i]= "n"

print("")
print(mediciones)
print("Hemos terminado de procesar las mediciones de voltaje")
