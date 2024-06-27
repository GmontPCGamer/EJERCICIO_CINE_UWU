import os
import msvcrt
import csv
from fun import *

while True:

    print(">>>Menu<<<")
    print("1) Mostrar asientos")
    print("2) comprar entrada")
    print("3) mostrar ventas realizadas")
    print("4) Generar archivo CSV")
    print("5) salir.")
    opc = int(input("seleccione opcion en pantalla: "))
    os.system('cls')
    if opc == 1:
       opc_1()
    elif opc == 2:
       opc_2()
    elif opc == 3:
        opc_3()
    elif opc == 4: 
        with open
    else:
        break                               