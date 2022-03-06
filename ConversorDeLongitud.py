from email import message
from email.policy import default
from sqlite3 import Row
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import font
from turtle import width
from unittest import result
ventana = Tk()

ventana.title("Converso de Longitud")
ventana.geometry()

# --funciones


def resultado():

    num_ingresado = int(entrada_texto1.get())
    unidad1 = var1.get()
    unidad2 = var2.get()

    unidades = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
    pos1 = unidades.index(unidad1)+1
    pos2 = unidades.index(unidad2)+1

    if pos1 < pos2:
        
        operacion = num_ingresado*(10**(pos2-pos1))
        etiqueta_resultado["text"] = operacion,unidad2

    elif pos2<pos1:
        operacion = num_ingresado/(10**(pos1-pos2))
        etiqueta_resultado["text"] = operacion,unidad2    
        
#funciones barra de menu
def salir():
    desicion = messagebox.askquestion("Salir","Desea salir de la aplicacion?")
    if desicion == "yes":
        ventana.destroy()

def Info():
    messagebox.showinfo("Info","Autor: Jose David Suarez Cardona")

def Version():
    messagebox.showinfo("Version","Version: 1.1")


# --Barra menu
barramenu = Menu(ventana)#se crea la barra de menu
mnu_Informacion =Menu(barramenu,tearoff=0)#creo un menu
#se crean las opciones del menu 
mnu_Informacion.add_command(label="Version",command=Version)
mnu_Informacion.add_command(label="Info",command=Info)

mnu_opciones = Menu(barramenu,tearoff=0)
mnu_opciones.add_command(label="Salir",command=salir)

barramenu.add_cascade(label="Informacion",menu=mnu_Informacion)
barramenu.add_cascade(label="opciones",menu=mnu_opciones)

ventana.config(menu=barramenu)


# --entradas de texto
entrada_texto1 = Entry(ventana, font={"Calibri 20"},background="grey")
entrada_texto1.grid(row=0, column=0, rowspan=4, padx=1, pady=1)
# --menus despplegables
var1 = tk.StringVar(ventana)
var1.set("km")
opciones1 = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
menu__1 = tk.OptionMenu(ventana, var1, *opciones1)
menu__1.config(width=10, height=2,font=20)
menu__1.grid(row=6, column=0)

var2 = tk.StringVar(ventana)
var2.set("km")
opciones2 = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
menu__2 = tk.OptionMenu(ventana, var2, *opciones2)
menu__2.config(width=10, height=2,font=20)
menu__2.grid(row=6, column=4)
menu__2.config(background="grey")


# --eBoton
flecha = Button(ventana, text="Convertir", width=8,
                height=2, command=resultado)
flecha.grid(row=6, column=1, padx=1)

# --etiquetas
etiqueta_resultado = Label(ventana, width=15, height=1, font={"Calibri 20"},background="grey")
etiqueta_resultado.grid(row=0, column=4)

etiqueta2 = Label(ventana)



ventana.config(background="black")
ventana.mainloop()
