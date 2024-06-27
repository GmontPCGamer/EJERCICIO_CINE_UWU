import os
import msvcrt
sala_de_cine = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
datos_personas = []

def opc_1():
    print(f"""\t>>>Pantalla<<<
        ================""")
    for x in range(len(sala_de_cine)):
        print(x+1,f"\t{sala_de_cine[x]}")
    print("\t================")
    print(">PRESIONE TECLA PARA CONTINUAR<")
    msvcrt.getch()

def opc_2():
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

def opc_3 ():
    c = 0
    for x in datos_personas:
        c =c+1
        print(f'{x['nombre'],x["numero_t"]}')
    print('total de entradas compradas es:', c)
    print('>>>PRESIONE TECLA PARA CONTINUAR<<<')
    msvcrt.getch()

