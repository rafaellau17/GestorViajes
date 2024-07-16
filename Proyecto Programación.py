# -*- coding: utf-8 -*-
"""
VERSION FINAL CON GUARDADO CORREGIDO v1.4
"""

import random as rd

lista_de_servicios = []
lista_de_ventas = []

def main():
    try:
        #Lee/Carga Servicios
        archivo = open("ArchivoProyectoServicios.txt", "r")
        for linea in archivo:
            ServicioLineaLee = linea.strip().split("::")
            Servs = {}
            Servs["Tipo de Servicio"] = str(ServicioLineaLee[0])
            Servs["Código de Servicio"] = int(ServicioLineaLee[1])
            Servs["Descripción"] = str(ServicioLineaLee[2])
            Servs["Beneficio Tributario"] = bool(ServicioLineaLee[3])
            Servs["Precio sin IGV"] = int(ServicioLineaLee[4])
            lista_de_servicios.append(Servs)
        archivo.close()
    except FileNotFoundError:
        archivo = open("ArchivoProyectoServicios.txt", "w")
        archivo.close()

    try:
        #Lee/Carga Ventas
        archivo = open("ArchivoProyectoVentas.txt", "r")
        for linea in archivo:
            ServicioLineaLee = linea.strip().split("::")
            Vents = {}
            Vents["Número de Venta"] = int(ServicioLineaLee[0])
            Vents["Código de Servicio"] = int(ServicioLineaLee[1])
            Vents["Precio de Venta"] = float(ServicioLineaLee[2])
            Vents["Cantidad Vendida"] = int(ServicioLineaLee[3])
            Vents["Total de Venta"] = float(ServicioLineaLee[4])
            lista_de_ventas.append(Vents)
        archivo.close()
    except FileNotFoundError:
        archivo = open("ArchivoProyectoVentas.txt", "w")
        archivo.close()

    print("\nArchivos cargados correctamente.")


    #Menú
    opcion = 0
    while opcion != 9:
        print(f"\nLista de Servicios: {lista_de_servicios}")
        print(f"\nLista de Ventas: {lista_de_ventas}")

        #Escribe/Guarda automaticacmente Servicios
        archivo = open("ArchivoProyectoServicios.txt", "w")
        for servicio in lista_de_servicios:
            TipoServicio = servicio["Tipo de Servicio"]  #String
            CodigoServicio = servicio["Código de Servicio"]  #Numero
            DescripcionServicio = servicio["Descripción"] #String o Numero
            BeneficioServicio = servicio["Beneficio Tributario"] #Boole
            PrecioSinIGV = servicio["Precio sin IGV"] #String o Numero
            ServicioLinea = str(TipoServicio) + "::" + str(CodigoServicio) + "::" + str(DescripcionServicio) + "::" + str(BeneficioServicio) + "::" + str(PrecioSinIGV)
            archivo.write(f"{ServicioLinea}\n")  #Tipo::Codigo::Descripcion::Beneficio
        archivo.close()

        #Escribe/Guarda automaticamente Ventas
        archivo = open("ArchivoProyectoVentas.txt", "w")
        for venta in lista_de_ventas:
            NumeroVenta = venta["Número de Venta"]  #Numero
            CodigoVenta = venta["Código de Servicio"] #Numero
            PrecioVenta = venta["Precio de Venta"]   #Numero
            CantidadVenta = venta["Cantidad Vendida"]  #Numero
            TotalVenta = venta["Total de Venta"]  #Numero
            VentaLinea = str(NumeroVenta) + "::" + str(CodigoVenta) + "::" + str(PrecioVenta) + "::" + str(CantidadVenta) + "::" + str(TotalVenta)
            archivo.write(f"{VentaLinea}\n")
        archivo.close()
        print("\nArchivos guardados correctamente.")

        try:
            opcion = int(input(
                "\nIngrese una opción:\n"
                "[1] Ingresar un servicio.\n"
                "[2] Registrar una venta.\n"
                "[3] Modificar la cantidad de una venta.\n"
                "[4] Ordenar las ventas.\n"
                "[5] Buscar una venta.\n"
                "[6] Mostrar la venta mayor.\n"
                "[7] Borrar la información.\n" #función adicional
                "[9] Salir.\n"
                "\n$ "
            ))
            match opcion:
                case 1:
                    ingresar_servicio()
                case 2:
                    registrar_ventas()
                case 3:
                    modificar_ventas(lista_de_ventas)
                case 4:
                    ordenar_ventas()
                case 5:
                    buscar_ventas()
                case 6:
                    mostrar_venta_mayor()
                case 7:
                    borrar_informacion()
                case 9:
                    print("\nEl programa ha finalizado con éxito.\n")
                    break
                case _:
                    print("\nERROR: Ingrese una opción válida.\n")
        except ValueError:
            print("\nERROR: Ingrese una opción válida.\n")

#Parametros para servicio
def ingresar_servicio():
    servicio = ''
    while servicio != 'z':
        servicio = input(
            "\nA continuación, ingrese el tipo de servicio:\n"
            "[a] Viajes Nacionales.\n"
            "[b] Viajes Internacionales.\n"
            "[c] Paquetes Turísticos.\n"
            "[z] Retornar.\n"
            "\n$ "
        )

        match servicio:
            case 'a':
                agregar_servicio("Viaje Nacional")
                return
            case 'b':
                agregar_servicio("Viaje Internacional")
                return
            case 'c':
                agregar_servicio("Paquete Turístico")
                return
            case 'z':
                break
            case _:
                print("\nERROR: Ingrese una opción válida.")

#OPCIÓN SERVICIO - Crea un diccionario para lista de servicios
def agregar_servicio(servicio):
    print(f"\n{servicio.upper()}:")
    codigo = generar_codigo()
    print(f"Código de servicio: {codigo}")
    descripcion = input("Descripción: ")
    while True:
        beneficio_tributario = input("Beneficio tributario (Sí/No): ")
        beneficio_tributario = beneficio_tributario.title()
        match beneficio_tributario:
            case "Sí":
                beneficio_tributario = True
                break
            case "Si":
                beneficio_tributario = True
                break
            case "No":
                beneficio_tributario = False
                break
            case _:
                print("ERROR: Ingrese una opción válida.")
    precio_sin_igv = calcular_precio_sin_igv(servicio)
    print(f"Precio sin IGV: {precio_sin_igv}")
    lista_de_servicios.append({"Tipo de Servicio": servicio,
                               "Código de Servicio": codigo,
                               "Descripción": descripcion,
                               "Beneficio Tributario": beneficio_tributario,
                               "Precio sin IGV": precio_sin_igv})
    return

#Código aleatorio
def generar_codigo():
    while True:
        temp = rd.randint(30000, 80000)
        if temp % 5 == 0:
            codigo = temp
            return codigo

#Calcula precio sin igv segun la opción elegida
def calcular_precio_sin_igv(servicio):
    match servicio:
        case "Viaje Nacional":
            while True:
                temp = rd.randint(150, 350)
                if temp % 2 == 0:
                    precio = temp
                    return precio
        case "Viaje Internacional":
            while True:
                temp = rd.randint(380, 750)
                if temp % 3 == 0:
                    precio = temp
                    return precio
        case "Paquete Turístico":
            while True:
                temp = rd.randint(390, 855)
                if temp % 2 != 0:
                    precio = temp
                    return precio

#OPCIÓN VENTAS - Crea diccionario para lista ventas
def registrar_ventas():
    if len(lista_de_servicios) == 0:
        print("\nERROR: No hay servicios registrados.")
        return
    while True:
        try:
            codigo = int(input("\nIngrese el código del servicio a registrar una venta: "))
            for servicio in lista_de_servicios:
                if servicio["Código de Servicio"] == codigo:
                    numero_venta = len(lista_de_ventas) + 1
                    print(f"Número de Venta: {numero_venta}")
                    if servicio["Beneficio Tributario"] == True:
                        precio_venta = servicio["Precio sin IGV"]
                    else:
                        precio_venta = round(servicio["Precio sin IGV"] * 1.18, 2)
                    print(f"Precio de Venta: {precio_venta:.2f}")
                    cantidad_venta = 0
                    while cantidad_venta < 1 or cantidad_venta > 10:
                        try:
                            cantidad_venta = int(input("Cantidad Vendida (1-10): "))
                            if cantidad_venta < 1 or cantidad_venta > 10:
                                print("ERROR: Ingrese una cantidad válida (1-10).")
                        except ValueError:
                            print("ERROR: Ingrese un valor válido.")
                    total_venta = round(cantidad_venta * precio_venta, 2)
                    print(f"Total de Venta: {total_venta:.2f}")
                    lista_de_ventas.append({"Número de Venta": numero_venta,
                                            "Código de Servicio": servicio["Código de Servicio"],
                                            "Precio de Venta": precio_venta,
                                            "Cantidad Vendida": cantidad_venta,
                                            "Total de Venta": total_venta})
                    return
            print("\nERROR: El código no ha sido encontrado.")
        except ValueError:
            print("\nERROR: Ingrese un valor numérico válido.")


def modificar_ventas(lista_de_ventas):
    if len(lista_de_ventas) == 0:
                print("\nERROR: No hay ventas registradas.")
                return
    quicksort(lista_de_ventas)
    pos = -1
    while True:
        try:
            numero_venta_original = int(input("\nIntroduzca el número de la venta a modificar: "))
            if numero_venta_original > len(lista_de_ventas):
                print("\nERROR: El valor ingresado no existe.")
                modificar_ventas(lista_de_ventas)
            #Busqueda binaria - Retorna la Posición del diccionario buscado
            izq = 0
            der = len(lista_de_ventas) - 1
            while izq <= der:
                medio = (izq + der) // 2
                if numero_venta_original == lista_de_ventas[medio]["Número de Venta"]:
                    pos = medio
                    break
                else:
                    if numero_venta_original < lista_de_ventas[medio]["Número de Venta"]:
                        der = medio - 1
                    else:
                        izq = medio + 1
            print(lista_de_ventas[pos])
            #n numero_venta_modificado = Cantidad de venta
            numero_venta_modificado = 0
            while numero_venta_modificado < 1 or numero_venta_modificado > 10:
                try:
                    numero_venta_modificado = int(input("Introduzca el nuevo valor de la cantidad vendida: "))
                    if numero_venta_modificado < 1 or numero_venta_modificado > 10:
                        print("ERROR: Ingrese una cantidad válida (1-10).")
                except ValueError:
                    print("ERROR: Ingrese un valor numérico válido.")
            #Actualiza la venta
            lista_de_ventas[pos]["Cantidad Vendida"] = numero_venta_modificado
            lista_de_ventas[pos]["Total de Venta"] = round(lista_de_ventas[pos]["Precio de Venta"] * lista_de_ventas[pos]["Cantidad Vendida"], 2)
            print(lista_de_ventas[pos])
            print("Número de venta actualizado correctamente.")
            return
        except IndexError:
            print("\nERROR: No se ha encontrado la venta.")
        except ValueError:
            print("\nERROR: Ingrese un valor numérico válido.")


#Ordena la lista de ventas por Total de ventas
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        menores = []
        mayores = []
        for i in range(1, len(lista)):
            if lista[i]["Número de Venta"] > pivot["Número de Venta"]:
                mayores.append(lista[i])
            else:
                menores.append(lista[i])
        mayores = quicksort(mayores)
        menores = quicksort(menores)
        lista_de_ventas = []
        lista_de_ventas.append(menores)
        lista_de_ventas.append(pivot)
        lista_de_ventas.append(mayores)
        return lista_de_ventas

#OPCIÓN 4 - Ordena la lista de ventas de mayor a menor según Total de venta
def ordenar_ventas():
    if len(lista_de_ventas) == 0:
                print("\nERROR: No hay ventas registradas.")
                return
    for i in range(len(lista_de_ventas) - 1):
        for j in range(len(lista_de_ventas) - 1 - i):
            if(lista_de_ventas[j]["Total de Venta"] < lista_de_ventas[j + 1]["Total de Venta"]):
                aux = lista_de_ventas[j + 1]
                lista_de_ventas[j + 1] = lista_de_ventas[j]
                lista_de_ventas[j] = aux
    print("\nLas ventas han sido ordenadas correctamente.")
    return lista_de_ventas

#OPCIÓN 5 - Busca diccionario/venta por número de venta
def buscar_ventas():
    if len(lista_de_ventas) == 0:
                print("\nERROR: No hay ventas registradas.")
                return
    while True:
        try:
            numero_venta = int(input("\nIngrese el número de venta a buscar: "))
            longitud = len(lista_de_ventas)
            buscado = numero_venta
            indice = 0
            for x in range(0, longitud):
                if lista_de_ventas[x]["Número de Venta"] == buscado:
                    indice = x
                    print(lista_de_ventas[indice])
                    return
            print("\nERROR: El número de venta no ha sido encontrado.")
            return
        except ValueError:
            print("\nERROR: Ingrese un valor numérico válido.")

#OPCIÓN 6 - Busca el diccionario/venta con mayor Total de venta
def mostrar_venta_mayor():
    if len(lista_de_ventas) == 0:
                print("\nERROR: No hay ventas registradas.")
                return
    mayor = 0
    for valor_venta in lista_de_ventas:
        if valor_venta["Total de Venta"] > mayor:
            mayor = valor_venta["Total de Venta"]
    for venta in lista_de_ventas:
        if mayor == venta["Total de Venta"]:
            print(f"\nVenta mayor: {venta}")
            return

#OPCIÓN 7 - Borra el contenido de los archivos de texto
def borrar_informacion():
    lista_de_servicios.clear()
    lista_de_ventas.clear()
    print("\nDatos eliminados correctamente.")


if __name__ == "__main__":
    main()