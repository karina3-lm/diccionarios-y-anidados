#diccionario españo-ingles
diccionario={}
Palabras_español=input("Escribe las palabras en el formato: - hola:hello,perro:dog,casa:house -" )
diccionario=Palabras_español
for x in Palabras_español.split(" , "):
  frase=input("Escriba una Frase en español para traducir: " )
for j in frase.split( ", " ):
    traduccion=diccionario
    if traduccion:
        print(traduccion)
    