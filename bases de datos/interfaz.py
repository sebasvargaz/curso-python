import sqlite3
from tkinter import * 

#raiz

root = Tk()
root.title("R I A Ñ O  GOURMET  - Menú")
root.resizable(0,0)
root.config(bd=25, relief="sunken")

Label(root, text="   R I A Ñ O GOURMET   ", fg="darkgreen", font=("Times New Roman",28, "bold italic")).pack()
Label(root, text="Menú del día", fg="green", font=("Times New Roman",24, "bold italic")).pack()

#separacion
Label(root, text="").pack()

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

#Buscar categorias

categorias = cursor.execute("SELECT * FROM categoria").fetchall()  
for categoria in categorias:
    Label(root, text=categoria[1], fg="black", font=("Times New Roman",20, "bold italic")).pack()
    platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
    for plato in platos:
        Label(root, text=plato[1], fg="gray", font=("Verdana", 15, "italic")).pack()
    Label(root, text="").pack()

conexion.close()

Label(root, text="$15.000 (IVA incl.)", fg="darkgreen", font=("Verdana", 15, "bold italic")).pack(side="right")

root.mainloop()
