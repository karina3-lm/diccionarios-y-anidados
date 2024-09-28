#registro de temperatura
tuplas=()
for i in range(0,7):
      dia=input("ingrese la el dia: " )
      tem=int(input("ingrese la temperatura: " ))
      tuplas+=(dia,tem,)
print(tuplas)