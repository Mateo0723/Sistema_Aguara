from tkinter import *
from tkinter.ttk import *

obras = ("Colón 8 viviendas", "Obra 15", "Obra 23")

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


date = Label(window, text="Fecha:")
date.grid(column=0, row=2)
date_value = Entry(
    validate="key",
    # We only need "%P".
    validatecommand=(window.register(validate_date), "%P"),
)
date_value.grid(column=1, row=2)

bill = Label(window, text="Nro de factura:")
bill.grid(column=4, row=2)
bill_value = Entry(window)
bill_value.grid(column=5, row=2)

type = Label(window, text="Tipo de factura:")
type.grid(column=9, row=2)
type_value = Combobox(window, state="readonly")
type_value["values"] = ("A", "B", "C")
type_value.current(0)
type_value.grid(column=10, row=2)

supplier = Label(window, text="Proveedor:")
supplier.grid(column=14, row=2)
supplier_value = Combobox(window, state="readonly")
supplier_value["values"] = ("Hierro San José", "Proveedor 1", "Proveedor 2")
# supplier_value.current(0)
supplier_value.grid(column=15, row=2)

# unidad, concepto, cantidad, precio_u, obra

unit = Label(window, text="Unidad:", padding=10)
unit.grid(column=0, row=4)
unit_value = Entry(window)
unit_value.grid(column=1, row=4)

concept = Label(window, text="Concepto:", padding=10)
concept.grid(column=4, row=4)
concept_value = Entry(window)
concept_value.grid(column=5, row=4)

# def print_invoice_data():
#    print("Número de factura:" + bill_value.get())
# print("Fecha de emisión:", invoice_date.get())
# print("Cliente:", client_name.get())
# print("Concepto:", concept.get())
# print("Monto:", amount.get())


# Botón para imprimir los datos ingresados
# submit_button = Button(window, text="Imprimir factura", command=print_invoice_data)
# submit_button.grid(row=5, column=1)

# Ejecutar ventana principal
window.mainloop()
