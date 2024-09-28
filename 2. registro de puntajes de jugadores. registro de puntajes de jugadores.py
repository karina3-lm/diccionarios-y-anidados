#registro de puntajes de jugadores
jugadores ="alan 3, Luis 4, Manuel 10, Enrique 8"
quitar=":.,/"
for caracter in quitar:
     jugadores=jugadores.replace(caracter,  
                                 "")
jugadores=jugadores.lower()
puntaje=jugadores.split()
puntaje_de_jugadores=[jugadores]
diccionario=jugadores
print(f"nombre del jugadro ’{jugadores}’ su puntaje {puntaje}")

##
Lista=["Luis",3, "Juan",10, "Pedro",3 ]
Diccionario=Lista
print(diccionario)

