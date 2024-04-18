from tkinter import * 
from tkinter import filedialog as FileDialog 
from io import open

ruta = ""  #almacenar ruta de fichero

def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Mi editor")

def abrir():
    mensaje.set("Abrir fichero")
    global ruta
    ruta = FileDialog.askopenfilename(
        initialdir='.', 
        filetypes=(("Ficheros de texto", "*.txt"),), 
        title="Abrir un fichero de texto")
    
    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, END)
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - Mi editor")

def guardar():
    if ruta != "":
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        guardarcomo()

def guardarcomo():
    global ruta
    mensaje.set("Guardar fichero como")
    fichero =FileDialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, 'end-1c')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else: 
        mensaje.set("Guardado cancelado")
        ruta = ""
        

#Config raiz 

root = Tk()
root.title("Mi editor")


#Menu superior 

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command= abrir)
filemenu.add_command(label="Guardar", command= guardar)
filemenu.add_command(label="Guardar como", command=guardarcomo)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=filemenu)

texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

mensaje = StringVar()
mensaje.set("Bienvenido a un editor mejor que word")
monitor = Label(root,textvar=mensaje, justify='left')
monitor.pack(side="left")


root.config(menu=menubar)

#final app 
root.mainloop()
