import os
import msvcrt
import csv
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
    while True:
        nombre = input("ingrese su nombre: ")
        if len(nombre) > 3:
            break
    while True:
        try:
            edad = int(input("ingrese su edad: "))
            if edad > 0 and edad < 120:
                break
            else:
                print('ERROR SU EDAD DEBE SER MAYOR A 0')
        except:
            print('ERROR DEBE SER UN NUMERO ENTERO')
    while True:
        try:
            numero_t = int(input("Ingrese su número de teléfono: +569"))
            if len(str(numero_t)) == 8:
                break
            else:
                print('ERROR: Su número de teléfono debe tener exactamente 8 números después de +569.')
        except ValueError:
            print('ERROR: Debe ingresar un número entero.')

    datos_persona = {"nombre": nombre,
        "edad" : edad, 
        "numero_t": numero_t}
    datos_personas.append(datos_persona)

    while True:
        try:
            c = int(input("escoja la Columna 1 a 5:"))
        except:
            print('ERROR DEBE SER UN NUMERO ENTERO')
        if c in range(1,6):
            break
    while True:
        try:
            p = int(input("escoja el asiento del 1 al 5: "))
        except:
            print('ERROR DEBE SER UN NUMERO ENTERO')
        if p in range(1,6):
            break

    sala_de_cine[c-1][p-1]= "x"

def opc_3 ():
    c = 0
    for x in datos_personas:
        c =c+1
        print(f'{x['nombre'],x["numero_t"]}')
    print('total de entradas compradas es:', c)
    print('>>>PRESIONE TECLA PARA CONTINUAR<<<')
    msvcrt.getch()

def opc_4 ():
    csv_registro = 'datos_personas.csv'
    fieldnames = ["nombre", "edad", "numero_t"]
    with open(csv_registro, mode='w', newline='') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=fieldnames)
        escritor.writeheader()
        escritor.writerows(datos_personas)
    print(f"Datos guardados en {csv_registro}")
    print('>>>PRESIONE TECLA PARA CONTINUAR<<<')
    msvcrt.getch()
