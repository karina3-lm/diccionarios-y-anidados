#Agenda de contactos
agenda={"Karina":[12-34-56-43-21],
            "Jose":[23-43-56-12-87],
            "Maria":[32-11-22-55-66]}
for c in agenda:
    nombre=input("ingrese nombre del contacto")
    if nombre in agenda:
      print("{} ya registrado, su numero {}".format(nombre,agenda[nombre]))
    else:
        agenda[nombre]=input("Indique el numero de telefono: ")
print("listado de contactos")
for nombre, numero in agenda.items():
 print(nombre,"----",numero)