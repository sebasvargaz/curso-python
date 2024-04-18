from tkinter import * 

root = Tk()
root.config(bd=15)

def sumar ():
    r.set(float(n1.get())+ float(n2.get()))
    borrar()

def restar():
        r.set(float(n1.get()) - float(n2.get()))
        borrar()

def multiplicar():
        r.set(float(n1.get()) * float(n2.get()))
        borrar()


    
def borrar():
    n1.set("")
    n2.set("")


n1 = StringVar()
n2 = StringVar()
r = StringVar()


Label(root, text="Número 1").pack()
Entry(root, justify="center",textvariable= n1).pack()  #numero 1
Label(root, text="Número 2").pack()
Entry(root, justify="center",textvariable= n2).pack() #numero 2
Label(root, text=" ").pack()
Button(root, text="Sumar", command=sumar).pack()
Button(root, text="Restar", command=restar).pack()
Button(root, text="Multiplicar", command=multiplicar).pack()
Label(root, text=" ").pack()
Label(root, text="El resultado es: ").pack() 
Entry(root, justify="center",textvariable= r, state="disabled").pack()  #resultado



root.mainloop()