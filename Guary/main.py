import tkinter as tk


class FacturaApp:
    def __init__(self, master):
        self.master = master
        master.title("Agüara Constructora S.A.")

        # Crear widgets de entrada de datos de factura
        tk.Label(master, text="Nombre del producto:").grid(row=0, column=0)
        self.producto_entry = tk.Entry(master)
        self.producto_entry.grid(row=0, column=1)

        tk.Label(master, text="Cantidad:").grid(row=1, column=0)
        self.cantidad_entry = tk.Entry(master)
        self.cantidad_entry.grid(row=1, column=1)

        tk.Label(master, text="Precio unitario:").grid(row=2, column=0)
        self.precio_entry = tk.Entry(master)
        self.precio_entry.grid(row=2, column=1)

        tk.Button(master, text="Agregar",
                  command=self.agregar_factura).grid(row=3, column=1)

        # Crear widgets para ver gastos
        tk.Label(master, text="Gastos totales:").grid(row=4, column=0)
        self.gastos_label = tk.Label(master, text="0")
        self.gastos_label.grid(row=4, column=1)

        # Crear widgets para ver stock
        tk.Label(master, text="Stock disponible:").grid(row=5, column=0)
        self.stock_label = tk.Label(master, text="0")
        self.stock_label.grid(row=5, column=1)

    def agregar_factura(self):
        # Obtener datos de entrada de datos de factura
        producto = self.producto_entry.get()
        cantidad = int(self.cantidad_entry.get())
        precio = float(self.precio_entry.get())

        # Calcular gastos y stock
        gastos = cantidad * precio
        stock = cantidad

        # Actualizar widgets de gastos y stock
        gastos_totales = float(self.gastos_label["text"])
        gastos_totales += gastos
        self.gastos_label["text"] = str(gastos_totales)

        stock_disponible = int(self.stock_label["text"])
        stock_disponible += stock
        self.stock_label["text"] = str(stock_disponible)

        # Limpiar campos de entrada de datos de factura
        self.producto_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)


root = tk.Tk()
app = FacturaApp(root)
root.mainloop()
