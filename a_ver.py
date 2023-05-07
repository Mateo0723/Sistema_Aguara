import tkinter as tk


def show_bill(bill):
    # create main application window
    root = tk.Tk()

    # set title and dimensions of window
    root.title("Bill Details")
    width, height = 500, 800
    root.geometry(f"{width},{height}")

    label1 = tk.Label(root, text="ID:", font=('Consolas', 14))
    label2 = tk.Label(root, text="Amount:", font=('Consolas', 14))
    label3 = tk.Label(root, text="Description:", font=('Consolas', 14))
    label4 = tk.Label(root, text="Date:", font=('Consolas', 14))
    button1 = tk.Button(root, text="Close", command=root.quit)

    def update_widgets(*args):
        # retrieve bill's details from passed dictionaries and update widget texts accordingly
        id = bill["id"]
        amount = "${:,.2f}".format(float(bill["amount"]))
        description = " ".join([x[0] + ": " + x[1]
                               for x in bill["details"].items()])
        date = bill["date"][:10].capitalize() if bill["date"] else "-"

        label1["text"] = f"[{id}]\n {date}"
        label2["text"] += "\nAmount: $" + amount
        label3["text"] += "\nDetails: " + description

    label1.grid(columnspan=2, row=0)
    label2.grid(columnspan=2, row=1)
    label3.grid(columnspan=2, row=2)
    label4.grid(row=3, column=0)
    button1.grid(row=4, column=0)
    button1.pack(pady=(10, 0))

    # start event loop and update widgets once
    root.mainloop()
    root.update_idletasks()
    update_widgets(label1, label2, label3, label4)
