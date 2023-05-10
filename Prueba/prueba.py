from tkinter import *

from tkinter import Menu

window = Tk()

window.title("Welcome to LikeGeeks app")


def validate_entry(new_text):
    """
    Chequear que `new_text` esté en formato dd/mm/aaaa.
    """
    # Máximo de diez caracteres.
    if len(new_text) > 10:
        return False
    checks = []
    for i, char in enumerate(new_text):
        # En los índices 2 y 5 deben estar los caracteres "/".
        if i in (2, 5):
            checks.append(char == "/")
        else:
            # En el resto de los casos, la única restricción es que sean
            # números entre el 0 y el 9.
            checks.append(char.isdecimal())
    # `all()` retorna verdadero si todos los chequeos son verdaderos.
    return all(checks)


entry = Entry(
    validate="key",
    # Solo necesitamos "%P".
    validatecommand=(window.register(validate_entry), "%P"),
)

entry.grid(column=2, row=2)

menu = Menu(window)

new_item = Menu(menu)

new_item.add_command(label="New")

new_item.add_separator()

new_item.add_command(label="Edit")

menu.add_cascade(label="File", menu=new_item)

window.config(menu=menu)

window.mainloop()
