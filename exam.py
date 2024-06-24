import os
import msvcrt
import csv
sala_de_cine = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
datos_personas = []
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
        print(f"""\t>>>Pantalla<<<
            ================""")

        for x in range(len(sala_de_cine)):
            print(x+1,f"\t{sala_de_cine[x]}")
        print("\t================")
        print(">PRESIONE TECLA PARA CONTINUAR<")
        msvcrt.getch()
    elif opc == 2:
        nombre = input("ingrese su nombre: ")
        edad = int(input("ingrese su edad: "))
        numero_t = int(input("ingrese su numero de telefono: +569"))
        datos_persona = {"nombre": nombre,
                           "edad" : edad, 
                           "numero_t": numero_t}
        datos_personas.append(datos_persona)
        c = int(input("escoja la Columna 1 a 5:"))
        p = int(input("escoja el asiento del 1 al 5: "))
        sala_de_cine[c-1][p-1]= "x"
    elif opc == 3:
        for x in range(len(datos_personas)):
            if len(datos_personas[x]) < x:
                print(x)
    elif opc == 4:
        pass
    else:
        break