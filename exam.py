from fun import *
#FINALIZADOOOOOOOOOOOOOOO
while True:

    print(">>>Menu<<<")
    print("1) Mostrar asientos")
    print("2) comprar entrada")
    print("3) mostrar ventas realizadas")
    print("4) Generar archivo CSV")
    print("5) salir.")
    while True:
        try:
            opc = int(input("seleccione opcion en pantalla: "))
        except:
            print('ERROR DEBE SER UN NUMERO ENTERO')
        if opc in range(1,6):
            break
    os.system('cls')
    if opc == 1:
       opc_1()
    elif opc == 2:
       opc_2()
    elif opc == 3:
        opc_3()
    elif opc == 4: 
        opc_4()
    else:
        break                               