#contador de palabras 
texto= "Python es un lenguaje de programación de propósito general, multiplataforma y dinámico, que se utiliza para crear software, sitios web, automatizar tareas y analizar datos. Es considerado uno de los lenguajes de programación más populares en la actualidad, en parte por su facilidad de uso y versatilidad"
quitar=":.,/"
for caracter in quitar:
     texto=texto.replace(caracter,            
                         "")
texto=texto.lower()
palabra=texto.split()
diccionario_frecuencia={}
for palabra in palabra:
    if palabra in diccionario_frecuencia:
        diccionario_frecuencia[palabra]+=1
    else:
        diccionario_frecuencia[palabra]=1
for palabra in diccionario_frecuencia:
    frecuencia=diccionario_frecuencia[palabra]
    print( f"{palabra}’ {frecuencia}")