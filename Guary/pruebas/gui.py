import tkinter as tk

# Crear ventana principal
root = tk.Tk()
root.title("Factura")

frame = tk.Frame(root, width=100, height=100, bg="gray")
frame.grid(row=0, column=0)

# Cambiar esto, no se si convendrá hacerlo en función porque hay que acceder a la variable para ver que se escribió.
# O hacerlo en función pero pasando la variable como parámetro, pinta.


def etiqueta_y_entrada(texto, rc_label, rc_grid):
    tk.Label(root, text=texto).grid(row=rc_label[0], column=rc_label[1])
    invoice_num = tk.Entry(root)
    invoice_num.grid(row=rc_grid[0], column=rc_grid[1])


# fecha, factura_tipo, factura_nro, proveedor, unidad, concepto, cantidad, precio_u, obra
# Crear etiquetas y entradas de datos
etiqueta_y_entrada("Nro de factura:", [0, 0], [0, 1])
etiqueta_y_entrada("Fecha de emisión", [0, 2], [0, 3])
# etiqueta_y_entrada("Tipo ")

tk.Label(root, text="Cliente:").grid(row=2, column=0)
client_name = tk.Entry(root)
client_name.grid(row=2, column=1,)

tk.Label(root, text="Concepto:").grid(row=3, column=0)
concept = tk.Entry(root)
concept.grid(row=3, column=1)

tk.Label(root, text="Monto:").grid(row=4, column=0)
amount = tk.Entry(root)
amount.grid(row=4, column=1)

# Función para imprimir los datos ingresados en la consola


def print_invoice_data():
    print("Número de factura:", invoice_num.get())
    print("Fecha de emisión:", invoice_date.get())
    print("Cliente:", client_name.get())
    print("Concepto:", concept.get())
    print("Monto:", amount.get())


# Botón para imprimir los datos ingresados
submit_button = tk.Button(root, text="Imprimir factura",
                          command=print_invoice_data)
submit_button.grid(row=5, column=1)

# Ejecutar ventana principal
root.mainloop()
