from tkinter import *

raiz = Tk()
raiz.title("Posicionamiento")
raiz.iconbitmap("Python-logo-notext.svg.ico")
raiz.geometry("400x200")
raiz.config(bg="gray")

def Sumar():
    n1 = float(txt1.get()) #txt1 se define posteriormente como un objeto (caja de texto), con el metodo get() sacamos su valor
    n2 = float(txt2.get())
    resultado = n1 + n2

    #Ahora debemos escribir el resultado en el espacio adecuado
    txt3.delete(0,"end") #Primero nos aseguramos que la caja donde escribiremos este vacia
                         # el metodo delete() borra lo que este escrito en una caja de texto, los parametros son donde comienza
                         # y donde termina a borrar
    txt3.insert(0, resultado) #Con el metodo insert estamos escribiendo dentro de una caja de texto, los parametros son
                              # primero a partir de que pixel empezamos a escribir dentro de la caja y luego lo que escribiriremos

#Ahora que esta creada la ventana inicial, lo ideal seria agregrale los widgets que haran el funcionamiento de la interfaz
#Antes de agregar cualquier widget debemos tener claro que siempre se le debe indicar la posicion de esté dentro del contenedor
# para resaltarle su posicion existen varios metodos, que no deben ser mezclados entre si al estar posicionando dentro de un mismo
# contenedor

#Primero creamos el widget, en este caso un label --> se crea como un objeto, haciendo uso de la clase Label()
lbl1 = Label(raiz, text="Primer numero", bg="light blue") 
lbl1.place(x=10,y=10, width=100, height=30) #Usaremos el metodo place() donde x, y indican la posicion del objeto respecto a su 
                                            # contenedor, como si de un plano cartesiano se tratase. Posteriormente estan la altura
                                            # y el ancho del objeto
lbl2 = Label(raiz, text="Segundo numero", bg="light blue") 
lbl2.place(x=10,y=50, width=100, height=30)

lbl3 = Label(raiz, text="Resultado", bg="light blue") 
lbl3.place(x=10,y=120, width=100, height=30)

#Para crear una caja de texto
txt1 = Entry(raiz, bg="blue") #Clase --> Entry()
txt1.place(x=120,y=10, width=100, height=30)
txt2 = Entry(raiz,bg="blue")
txt2.place(x=120,y=50, width=100, height=30)
txt3 = Entry(raiz,bg="blue")
txt3.place(x=120,y=120, width=100, height=30)

#Para crear botones -- vea que para a un boton se le debe indicar su funcionalidad a traves de una funcion     
btn1 = Button(raiz,text="Sumar",command=Sumar)
btn1.place(x=230,y=50, width=80, height=30)

#CADA UNA DE LAS MEDIDAS EN PIXELES DEL METODO DE PLACE(), PUEDE SER CAMBIADO POR SUS VALORES RELATIVOS 0-1
#POR EJEMPLO : EN VEZ DE X, PONER EL PARAMETRO RELX = 0.1, EN ESE CASO EL OBJETO SE UBIACARA PARA EL EJE X 
#EL 10% DEL TAMAÑO DEL CONTENEDOR        

raiz.mainloop()