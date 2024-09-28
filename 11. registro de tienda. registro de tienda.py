# registro de tienda
compra=()
for i in range(0,3):
    producto=input("ingrese el producto: " )
    cantidad=int(input("ingrese cantidad: " ))
    precio=float(input("ingrese el precio: " ))
    total=cantidad*precio
    print("total de la compra: ", total)
    total_C=0+total
    print("total de la compra acumulada: ", total_C)
    compra+=(producto, cantidad, precio, total,)
    print(compra,total_C)