#diccionario de notas
diccionario={}
estudiantes=input("ingrese el nombre del estudiante: " )
for x in estudiantes.split(" , "):
 if x in estudiantes:
        notas=input("ingrese la calificacion del estudiante: ")
        diccionario[estudiantes]=notas
print(diccionario)

