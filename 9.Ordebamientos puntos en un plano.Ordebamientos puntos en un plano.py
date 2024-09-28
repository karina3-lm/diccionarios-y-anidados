#ordenamiento puntos en un plano
tuplas=()
punto_1=int(input(" ingrese el punto x " ))
punto_2=int(input(" ingrese el punto: y " ))
punto_3=int(input(" ingrese el punto: x " ))
punto_4=int(input(" ingrese el punto: y " ))
punto_5=int(input(" ingrese el punto x " ))
punto_6=int(input(" ingrese el punto y " ))

tuplas=(punto_1, punto_2),    (punto_3, punto_4),  (punto_5, punto_6)

print(sorted(tuplas, key=lambda x: x[0]))