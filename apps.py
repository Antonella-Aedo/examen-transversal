from utilidades import menu,reporte_sueldos,estadistica,clasificar_sueldos, generar_sueldos
lista=[]
while True:
    try:
        menu()
        op=int(input("ingrese la opcion a elegir "))
        if op==1:
            generar_sueldos(lista)
        elif op ==2:
            clasificar_sueldos(lista)
        elif op==3:
            estadistica(lista)
        elif op==4:
            reporte_sueldos(lista)
        elif op==5:
            break
        else:
            print("Opcion invalida, ingrese opcion  1 - 5")
    except ValueError:
        print("ingrese solo numeros enteros")