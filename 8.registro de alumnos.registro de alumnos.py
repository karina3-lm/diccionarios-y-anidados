#registro de alumnos
registro_alumnos={}
for i in range (0,5):
    nombre=input("ingresa el nombre: " )
    edad=int(input("ingrese edad: " ))
    cal=int(input("ingrese cal"))
    registro_alumnos[nombre]={"edad":edad, "calificacion":cal}
print(registro_alumnos)