
from tkinter import Tk, Label, Button,Entry, Frame, END
import pandas as pd

ventana = Tk()
ventana.config(bg='black')
ventana.geometry('560x260')
ventana.resizable(0,0)
ventana.title('Red Social UNO')
nombre1,gradoAmistad,nombre2= [],[],[]

def agregar_datos():
	global nombre1, gradoAmistad, nombre2

	nombre1.append(ingresa_nombre.get())
	gradoAmistad.append(ingresa_grado.get())
	nombre2.append(ingresa_nombre2.get())
	
	ingresa_nombre.delete(0,END)
	ingresa_grado.delete(0,END)
	ingresa_nombre2.delete(0,END)
	

def guardar_datos():	
	global nombre1,gradoAmistad,nombre2

	datos = {'Primera persona':nombre1,'Grado de amistad':gradoAmistad, 'Segunda persona':nombre2 } 
	nom_excel  = str(nombre_archivo.get() + ".xlsx")	
	df = pd.DataFrame(datos,columns =  ['Primera persona', 'Grado de amistad', 'Segunda persona']) 
	df.to_excel(nom_excel)
	nombre_archivo.delete(0,END)

frame1 = Frame(ventana, bg='black')
frame1.grid(column=0, row=0, sticky='nsew')
frame2 = Frame(ventana, bg='black')
frame2.grid(column=1, row=0, sticky='nsew')

nombre = Label(frame1, text ='Nombre y apellido', width=14).grid(column=0, row=0, pady=20, padx= 10)
ingresa_nombre = Entry(frame1,  width=20, font = ('Arial',10))
ingresa_nombre.grid(column=1, row=0)

grado = Label(frame1, text ='Grado de amistad', width=14).grid(column=0, row=1, pady=20, padx= 10)
ingresa_grado = Entry(frame1, width=20, font = ('Arial',10))
ingresa_grado.grid(column=1, row=1)

nombreSegundo = Label(frame1, text ='Nombre y apellido', width=14).grid(column=0, row=2, pady=20, padx= 10)
ingresa_nombre2 = Entry(frame1,  width=20, font = ('Arial',10))
ingresa_nombre2.grid(column=1, row=2)

agregar = Button(frame1, width=20, font = ('Arial',12, 'bold'), text='Agregar', bg='skyblue',bd=5, command =agregar_datos)
agregar.grid(columnspan=2, row=5, pady=20, padx= 10)

archivo = Label(frame2, text ='Ingrese Nombre del archivo', width=25, bg='gray16',font = ('Arial',12, 'bold'), fg='white')
archivo.grid(column=0, row=0, pady=10, padx= 10)

nombre_archivo = Entry(frame2, width=23, font = ('Arial',12))
nombre_archivo.grid(column=0, row=1, pady=1, padx= 10)

guardar = Button(frame2, width=20, font = ('Arial',12, 'bold'), text='Guardar', bg='skyblue',bd=5, command =guardar_datos)
guardar.grid(column=0, row=2, pady=20, padx= 10)



ventana.mainloop()