import random
import csv

def menu():
    print("menu")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas.")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

def generar_sueldos(lista):
    trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
    for i in range(len(trabajadores)):
        nombre=(f"trabajador: {trabajadores[i]}")
        sueldo=random.randint(300000,2500000)
        diccionario={
            'nombre':nombre,
            'sueldo':sueldo
        }
    lista.append(diccionario)
    print("se han generado los sueldos correspondiente a cada trabajador")
def clasificar_sueldos(lista):
    bajos=[]
    medios=[]
    altos=[]
    for i in lista:
        if i['sueldo']<=800000:
            bajos.append(i)
        elif i['sueldo']<=2000000:
            medios.append(i)
        else:
            altos.append(i)

    print("Sueldos menores a $800.000")
    for i in bajos:
        print(f"nombre: {i['nombre']} sueldo: {i['sueldo']}")
    
    print("Sueldos entre $800.000 y $2.000.000")
    for i in medios:
        print(f"nombre: {i['nombre']} sueldo: {i['sueldo']}")
    
    print("Sueldos superiores a $2.000.000") 
    for i in altos:
        print(f"nombre: {i['nombre']} sueldo: {i['sueldo']}")

def estadistica(lista):
    print(F"sueldos mas bajos:")
    print(F"sueldos mas alto: ")
    sueldos={sueldo['sueldo'] for sueldo in lista}
    promedio = sum(sueldos) / len(lista)
    print(f"sueldo promedio: {promedio}")
def reporte_sueldos(lista):
    lista_sueldos=[]
    for i in lista:
        sueldo_bruto= i["sueldo"]
        salud=int(sueldo_bruto * 0.7)
        afp=int(sueldo_bruto * 0.12)
        sueldo_liquido= sueldo_bruto-salud-afp
        dicci={
            'nombre': i["nombre"],
            'sueldo_bruto' : sueldo_bruto,
            'sueldo_liquido': sueldo_liquido
        }
    lista_sueldos.append(dicci)
    claves=dicci[0].keys()
    with open('sueldos.csv', 'w', newline="") as archivo:
        x=csv.dicwriter(archivo,fieldnames=claves)
        x.writerheader() #encabezados del archivo csv
        x.writerows(dicci)
       