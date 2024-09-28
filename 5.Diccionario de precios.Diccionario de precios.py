#diccionario de precios
productos={"refresco": [30],
           "galletas":[25],
            "chocolate":[40],
            "sopas":[8]}
for i in productos:
    nombre=input("ingrese el nombre del producto a comprar: " )
    if nombre in productos:
       print("{}producto, su precio {}".format(nombre, productos[nombre]))
    else:
        print("producto no encontrado")
        agregar_producto(nombre,precio)
    for agregar_producto in productos:
        agregar_producto="producto_no_encontrado"
        nombre=input("agrege el nombre del producto: " )
        precio=float(input("agrege el precio del producto: " )) 
for producto, precio in productos.items():
    print(productos)