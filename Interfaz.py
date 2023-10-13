from tkinter import *
from numpy import sqrt

def calcular():
    valor_lado = float(lado.get())
    perimetro =  3*valor_lado
    caja3.insert(0, perimetro)

    altura = round(sqrt((valor_lado**2)-(valor_lado/2)**2), 2)
    area = round(valor_lado*altura*0.5, 2)
    caja2.insert(0, area)

def borrar():
    caja2.delete(0, "end")
    caja3.delete(0, "end")

ventana = Tk()
ventana.title("Area del triángulo")
ventana.geometry("650x550")
#ventana.config(bg="gray")

label1 = Label(ventana, text="Triángulo")
label1.place(relx=0.4,rely=0.1,relwidth=0.2,relheight=0.1)

label2 = Label(ventana, text="Lado: ")
label2.place(relx=0.3,rely=0.25,relwidth=0.2,relheight=0.1)

label3 = Label(ventana, text="Area: ")
label3.place(relx=0.3,rely=0.35,relwidth=0.2,relheight=0.1)

label4 = Label(ventana, text="Perimetro: ")
label4.place(relx=0.3,rely=0.5,relwidth=0.2,relheight=0.1)

lado = Entry(ventana)
lado.place(relx=0.5,rely=0.25,relwidth=0.2,relheight=0.1)

caja2 = Entry(ventana)
caja2.place(relx=0.5,rely=0.35,relwidth=0.2,relheight=0.1)

caja3 = Entry(ventana)
caja3.place(relx=0.5,rely=0.5,relwidth=0.2,relheight=0.1)

boton1 = Button(ventana, text="Calcular", command=calcular)
boton1.place(relx=0.35,rely=0.7,relwidth=0.2,relheight=0.1)

boton2 = Button(ventana, text="Borrar", command=borrar)
boton2.place(relx=0.6,rely=0.7,relwidth=0.2,relheight=0.1)
ventana.mainloop()