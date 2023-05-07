from datetime import datetime
import csv
import os


class Gasto:
    def __init__(self, fecha, factura_tipo, factura_nro, proveedor, unidad, concepto, cantidad, precio_u, obra, ubi):
        self.fecha = datetime.strptime(fecha, "%d/%m/%Y")
        self.factura_tipo = factura_tipo   # A
        self.factura_nro = factura_nro     # 123
        self.proveedor = proveedor         # Hierro San José
        self.unidad = unidad               # Bolsa de 50kg
        self.cantidad = cantidad           # 20
        self.concepto = concepto           # Cemento Avellaneda
        self.precio_u = precio_u           # 2000
        self.obra = obra                   # Obra 1
        self.ubi = ubi                     # Obra | Corralón | Depósito


class SistemaGestionGastos:
    def __init__(self):
        self.gastos = []
        self.obras = []
        self.stock = {}

    def agregar_gasto(self, gasto):

        datos = [gasto.fecha.strftime("%d/%m/%Y"), gasto.factura_tipo,
                 gasto.factura_nro, gasto.proveedor, gasto.unidad, gasto.cantidad,
                 gasto.concepto, gasto.precio_u, gasto.obra, gasto.ubi]

        csv_fecha = f'gastos_{gasto.fecha.year}.csv'
        csv_obra = f'gastos_{gasto.obra}.csv'

    # Verificar si el archivo ya existe
        if os.path.exists(csv_fecha):
            with open(csv_fecha, 'a', newline="") as archivo:
                escritor_csv = csv.writer(archivo)
                escritor_csv.writerow(datos)
        else:
            # Si el archivo no existe, crearlo y escribir en él
            with open(csv_fecha, 'w', newline='') as archivo:
                escritor_csv = csv.writer(archivo)
                escritor_csv.writerow(datos)

        if os.path.exists(csv_obra):
            with open(csv_obra, 'a', newline='') as archivo:
                escritor_csv = csv.writer(archivo)
                escritor_csv.writerow(datos)
        else:
            with open(csv_obra, 'w', newline='') as archivo:
                escritor_csv = csv.writer(archivo)
                escritor_csv.writerow(datos)

    def agregar_stock(self, gasto):

        datos = [gasto.fecha.strftime("%d/%m/%Y"), gasto.factura_tipo,
                 gasto.factura_nro, gasto.proveedor, gasto.unidad, gasto.cantidad,
                 gasto.concepto, gasto.precio_u, gasto.obra, gasto.ubi]

        csv_obra = f'stock_{gasto.obra}.csv'

        if os.path.exists(csv_obra):
            with open(csv_obra, 'a', newline='') as archivo:
                escritor_csv = csv.writer(archivo)
                escritor_csv.writerow(datos)
        else:
            with open(csv_obra, 'w', newline='') as archivo:
                escritor_csv = csv.writer(archivo)
                escritor_csv.writerow(datos)

    def gestionar_entrada(self, gasto):

        if gasto.ubi == 'Obra':
            self.agregar_gasto(gasto)
        else:
            self.agregar_stock(gasto)

    def obtener_gastos_totales(self, nombre):
        ruta = f'gastos_{nombre}.csv'
        gastos = []
        if os.path.exists(ruta):
            with open(ruta, 'r') as archivo:
                lector_csv = csv.reader(archivo)
                for fila in lector_csv:
                    if fila:
                        cantidad = int(fila[1])
                        precio_u = float(fila[3])
                        gastos.append(cantidad*precio_u)
                return sum(gastos)
        else:
            print(f'No se encuentra ningún dato sobre {nombre}')

    # pos es la posición del elemento a mover (primer elemento es pos = 1 (no 0))
    # cantidad_solicitada es la cantidad a mover
    # obra_giver es el gasto.obra de donde sale el stock
    # obra_receiver es el gasto.obra de donde llega el stock
    def cambiar_stock(self, pos, cantidad_solicitada, obra_giver, obra_receiver):
        with open(f'stock_{obra_giver}.csv', 'r') as archivo1:
            reader = csv.reader(archivo1)
            # Convertir el objeto reader en una lista
            filas = list(reader)
            elemento = filas[pos-1]
        # Falta corregir que no se permita una cantidad_solicitada > que la cantidad que hay
        if elemento[5] == cantidad_solicitada:

            del filas[pos-1]

        else:
            filas[pos-1][6] = int(filas[pos-1][6]) - cantidad_solicitada

        with open(f'stock_{obra_giver}.csv', 'w', newline='') as archivo2:
            writer = csv.writer(archivo2)
            writer.writerows(filas)

        elemento[6] = cantidad_solicitada
        elemento[8] = obra_receiver
        with open(f'stock_{obra_receiver}.csv', 'a', newline='') as archivo3:
            writer = csv.writer(archivo3)
            writer.writerow(elemento)


sistema_gastos = SistemaGestionGastos()
"""
# fecha, factura_tipo, factura_nro, proveedor, unidad, concepto, cantidad, precio_u, obra, ubicación
fecha1 = '27/04/2023'
tipo1 = 'A'
nro1 = '123456'
proveedor1 = 'Hierro San José'
unidad1 = 'Bolsa 50kg'
concepto1 = 'Cemento'
cantidad1 = 75
precio_u1 = 1900
obra1 = 'Obra Colón'
ubi1 = 'Depósito 25'  # o Depósito o Corralón(proveedor)

gasto1 = Gasto(fecha1, tipo1, nro1, proveedor1, unidad1,
               concepto1, cantidad1, precio_u1, obra1, ubi1)

sistema_gastos.gestionar_entrada(gasto1)
"""
# anio = '2023'
# print(   f'Los gastos de {anio} son {sistema_gastos.obtener_gastos_totales_por_anio(anio)}')

# self, pos, cantidad_solicitada, obra_giver, obra_receiver

sistema_gastos.cambiar_stock(3, 7, 'Obra 1', 'Obra 2')
