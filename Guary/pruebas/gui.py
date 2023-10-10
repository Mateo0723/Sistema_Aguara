from tkinter import *
from tkinter.ttk import *

obras = ("Colón 8 viviendas", "Obra 15", "Obra 23")

altura = 0.35
headlines = False

# Crear ventana principal
window = Tk()
window.title("Factura")
window.geometry("900x600")

# combo = Combobox(window, state="readonly")

# combo["values"] = obras
# combo.current(1)

# .grid(column=3, row=0)

# frame = Frame(window, width=100, height=100, bg="gray")
# frame.grid(row=0, column=0)


# Create function that validates dates:
def validate_date(new_text):
    """
    Check that `new_text` is in dd/mm/aaaa format.
    """
    # top 10 characters
    if len(new_text) > 10:
        return False
    checks = []
    for i, char in enumerate(new_text):
        # In index 2 and 5 must be "/".
        if i in (2, 5):
            checks.append(char == "/")
        else:
            # Otherwise chars must be numbers between 0 and 9
            checks.append(char.isdecimal())
    # `all()` returns true if all are true
    return all(checks)


date = Label(window, text="Fecha:", width=6)
date.place(relx=0.05, rely=0)
fecha_emision = Entry(
    validate="key",
    # We only need "%P".
    validatecommand=(window.register(validate_date), "%P"),
    width=10,
)
fecha_emision.place(relx=0.1, rely=0)

bill = Label(window, text="Nro de factura:", width=15)
bill.place(relx=0.2, rely=0)
nro_factura = Entry(window)
nro_factura.place(relx=0.3, rely=0)

type = Label(window, text="Tipo de factura:")
type.place(relx=0.45, rely=0)
tipo_factura = Combobox(window, state="readonly", width=3)
tipo_factura["values"] = ("A", "B", "C")
tipo_factura.current(0)
tipo_factura.place(relx=0.55, rely=0)

supplier = Label(window, text="Proveedor:")
supplier.place(relx=0.60, rely=0)
proveedor = Combobox(window, state="readonly")
proveedor["values"] = ("Hierro San José", "Proveedor 1", "Proveedor 2")
# supplier_value.current(0)
proveedor.place(relx=0.67, rely=0)

# unidad, concepto, cantidad, precio_u, obra

unit = Label(window, text="Unidad:")
unit.place(relx=0.05, rely=0.05)
unidad = Entry(window, width=10)
unidad.place(relx=0.1, rely=0.05)

concept = Label(window, text="Concepto:")
concept.place(relx=0.2, rely=0.05)
concepto = Entry(window, width=23)
concepto.place(relx=0.28, rely=0.05)

quantity = Label(window, text="Cantidad:")
quantity.place(relx=0.45, rely=0.05)
cantidad = Entry(window, width=10)
cantidad.place(relx=0.52, rely=0.05)

price = Label(window, text="Precio:", width=6)
price.place(relx=0.6, rely=0.05)
precio_u = Entry(window, width=10)
precio_u.place(relx=0.67, rely=0.05)


def imprimir_datos():
    print("Número de factura: " + nro_factura.get())
    print("Fecha de emisión: ", fecha_emision.get())
    print("Proveedor: ", proveedor.get())
    print("Concepto: ", concepto.get())
    print("Cantidad: ", cantidad.get())
    print("Precio por unidad: ", precio_u.get())
    print("Total: ", int(cantidad.get()) * float(precio_u.get()))


def agregar_linea():
    if not globals()["headlines"]:
        date0 = Label(window, text="Fecha", width=6)
        date0.place(relx=0.05, rely=0.3)
        concept0 = Label(window, text="Concepto", width=9)
        concept0.place(relx=0.12, rely=0.3)
        quantity0 = Label(window, text="Cantidad", width=9)
        quantity0.place(relx=0.4, rely=0.3)
        unit0 = Label(window, text="Unidad", width=7)
        unit0.place(relx=0.46, rely=0.3)
        precio_u0 = Label(window, text="Precio U.")
        precio_u0.place(relx=0.52, rely=0.3)
        total0 = Label(window, text="Total")
        total0.place(relx=0.6, rely=0.3)
        globals()["headlines"] = True
    date1 = Label(window, text=fecha_emision.get())
    date1.place(relx=0.05, rely=globals()["altura"])
    concept0 = Label(window, text=concepto.get())
    concept0.place(relx=0.12, rely=globals()["altura"])
    quantity0 = Label(window, text=cantidad.get())
    quantity0.place(relx=0.4, rely=globals()["altura"])
    unit0 = Label(window, text=unidad.get())
    unit0.place(relx=0.46, rely=globals()["altura"])
    precio_u0 = Label(window, text=precio_u.get())
    precio_u0.place(relx=0.52, rely=globals()["altura"])
    total0 = Label(window, text=int(cantidad.get()) * float(precio_u.get()))
    total0.place(relx=0.6, rely=globals()["altura"])
    globals()["altura"] = globals()["altura"] + 0.05


# Botón para imprimir los datos ingresados
submit_button = Button(window, text="Imprimir factura", command=imprimir_datos)
submit_button.place(relx=0.05, rely=0.1)

# Botón para agregar línea de factura
add_button = Button(window, text="Agregar línea", command=agregar_linea)
add_button.place(relx=0.2, rely=0.1)

# Ejecutar ventana principal
window.mainloop()
