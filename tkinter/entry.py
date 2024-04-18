from tkinter import * 

root = Tk()

label = Label(root, text="Nombre de chimba")
label.grid(row=0, column=0, sticky="w", pady=5)
entry = Entry(root)
entry.grid(row=0, column=1)


label2 = Label(root, text="Apellido")
label2.grid(row=1, column=0, sticky="e")
entry2 = Entry(root)
entry2.grid(row=1, column=1, pady=5)
entry2.config(justify="center", show="*")
root.mainloop()


