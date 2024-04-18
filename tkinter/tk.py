from tkinter import *

root = Tk()

root.title("Hola mundo mi primer IG")
root.iconbitmap("hola.ico")
root.resizable(1, 1)


frame = Frame(root, width=480, height=320)
frame.pack(anchor="center")
root.config(cursor="arrow")
root.config(bg="yellow")
root.config(bd=15)
root.config(relief="ridge")



root.mainloop()

