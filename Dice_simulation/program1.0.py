import random
import tkinter as tk
from tkinter import ttk
from tkinter import *
class Aplicacion: 
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.geometry("650x450")
        self.ventana1.resizable(0,0)
        self.ventana1.title("Dice Simulation")
        self.ventana1.iconbitmap("icon.ico")
        self.inicio=tk.Canvas(self.ventana1, width=650, height=450,bg="pink")
        self.titulo=Label(self.inicio,text="Dice Simulation",font=("Roman",22), bg="pink").place(x=220, y=100)
        self.boton1=ttk.Button(self.inicio, text="Lanzar", command=self.Lanzar)
        self.boton2=ttk.Button(self.inicio, text="salir", command=self.Salir)
        self.boton1.place(x=285,y=300)
        self.boton2.place(x=285,y=350)
        self.inicio.place(x=0,y=0)
        self.cara1=tk.PhotoImage(file="1.png")
        self.cara2=tk.PhotoImage(file="2.png")
        self.cara3=tk.PhotoImage(file="3.png")
        self.cara4=tk.PhotoImage(file="4.png")
        self.cara5=tk.PhotoImage(file="5.png")
        self.cara6=tk.PhotoImage(file="6.png")
        self.ventana1.mainloop()        

    def Lanzar(self):
        self.inicio.destroy()
        self.lanzar=tk.Canvas(self.ventana1, width=650, height=450, background="red")
        self.lanzar.place(x=0,y=0)
        self.titulo2=Label(self.lanzar,text="Dice",font=("Roman",22), bg="yellow").place(x=300, y=50)
        self.boton3=ttk.Button(self.lanzar, text="Lanzar", command=self.Arrojar)
        self.boton4=ttk.Button(self.lanzar, text="salir", command=self.Salir)
        self.boton3.place(x=285,y=300)
        self.boton4.place(x=285,y=350)
        valor=random.randint(1,6)
        if valor==1:
            self.lanzar.create_image(250,100, image=self.cara1, anchor="nw")
        if valor==2:
            self.lanzar.create_image(250,100, image=self.cara2, anchor="nw")
        if valor==3:
            self.lanzar.create_image(250,100, image=self.cara3, anchor="nw")
        if valor==4:
            self.lanzar.create_image(250,100, image=self.cara4, anchor="nw")
        if valor==5:
            self.lanzar.create_image(250,100, image=self.cara5, anchor="nw")
        if valor==6:
            self.lanzar.create_image(250,100, image=self.cara6, anchor="nw")

    def Arrojar(self):
        valor=random.randint(1,6)
        if valor==1:
            self.lanzar.create_image(250,100, image=self.cara1, anchor="nw")
        if valor==2:
            self.lanzar.create_image(250,100, image=self.cara2, anchor="nw")
        if valor==3:
            self.lanzar.create_image(250,100, image=self.cara3, anchor="nw")
        if valor==4:
            self.lanzar.create_image(250,100, image=self.cara4, anchor="nw")
        if valor==5:
            self.lanzar.create_image(250,100, image=self.cara5, anchor="nw")
        if valor==6:
            self.lanzar.create_image(250,100, image=self.cara6, anchor="nw")
        return valor
        
    def Salir(self):
        self.ventana1.destroy()

app1=Aplicacion()


#dado = randint(1, 6)
#print("Obtuviste: ",dado)

#dado2 = randint(1, 6)
#print("El bot Obtuvo: ", dado2)

#if dado < dado2:
#    print("Perdiste")
#else: 
#    if dado == dado2: 
#       print("Empate")
#    else : print("ganaste")

