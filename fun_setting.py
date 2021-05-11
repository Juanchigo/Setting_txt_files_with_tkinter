# -*- coding: utf-8 -*-
"""
Created on Mon May 10 12:56:59 2021

@author: Juanchi
"""
from tkinter import *
import numpy as np

###############################################################################
def MPC_INTA(tab,ruta):
    # Reading current values from the file to modify
    archivo = open(ruta,'r')
    p = carga(archivo)
    archivo.close()
    
    # Panel control
    param = LabelFrame(tab, text='Parámetros')
    param.grid(row=0, column=0, sticky=W, padx=10, pady=3)
    
    # ts ------------------------
    lbl = Label(param, text="ts")
    lbl.grid(column=0, row=1, sticky=W, padx=5, pady=2)
    
    txt = Entry(param,width=10)
    txt.grid(column=1, row=1)
    
    txt.insert(0,p[0,0])                # show current value
    
    lbl0 = Label(param, text="[s]")
    lbl0.grid(column=2, row=1)
    
    # N -------------------------
    lbl1 = Label(param, text="N")
    lbl1.grid(column=0, row=2, sticky=W, padx=5, pady=2)
    
    txt1 = Entry(param,width=10)
    txt1.grid(column=1, row=2)
    
    txt1.insert(0,p[1,0])
    
    # Nu -------------------------
    lbl2 = Label(param, text="Nu")
    lbl2.grid(column=0, row=3, sticky=W, padx=5, pady=2)
    
    txt2 = Entry(param,width=10)
    txt2.grid(column=1, row=3)
    
    txt2.insert(0,p[2,0])
    
    # alpha ---------------------
    lbl3 = Label(param, text="α")
    lbl3.grid(column=0, row=4, sticky=W, padx=5, pady=2)
    
    txt3 = Entry(param,width=10)
    txt3.grid(column=1, row=4)
    
    txt3.insert(0,p[3,0])
    
    # Beta1 ----------------------
    lbl4 = Label(param, text="B1")
    lbl4.grid(column=0, row=5, sticky=W, padx=5, pady=2)
    
    txt4 = Entry(param,width=10)
    txt4.grid(column=1, row=5)
    
    txt4.insert(0,p[4,0])
    
    # Beta2 ----------------------
    lbl5 = Label(param, text="B2")
    lbl5.grid(column=0, row=6, sticky=W, padx=5, pady=2)
    txt5 = Entry(param,width=10)
    txt5.grid(column=1, row=6)
    txt5.insert(0,p[5,0])
    
    # Button click function
    def clicked():
        contenido = txt.get()+ '\n' + txt1.get() + '\n' + txt2.get()+ '\n' + txt3.get() + '\n' + txt4.get() + '\n' + txt5.get()    
        archivo = open(ruta,'w')
        archivo.write(contenido)
        archivo.close()
        messagebox.showinfo('Parameter setting', 'Successfull Set')
    
    # Button
    btn = Button(tab, text="Set", command=clicked)
    btn.grid(column=2, row=0)

###############################################################################
def PID(tab,ruta):
    # Reading current values from the file to modify
    archivo = open(ruta,'r')
    p = carga(archivo)
    archivo.close()
    
    # Panel control
    param = LabelFrame(tab, text='Parámetros')
    param.grid(row=0, column=0, sticky=W, padx=10, pady=3)    
    
    # ts ------------------------
    lbl = Label(param, text="ts")
    lbl.grid(column=0, row=1, sticky=W, padx=5, pady=2)
    
    txt = Entry(param,width=10)
    txt.grid(column=1, row=1)
    
    txt.insert(0,p[0,0])
    
    lbl0 = Label(param, text="[s]")
    lbl0.grid(column=2, row=1)
    
    # Button click function
    def clicked():
        contenido = txt.get()
        archivo = open(ruta,'w')
        archivo.write(contenido)
        archivo.close()
        messagebox.showinfo('Parameter setting', 'Successfull Set')
    
    # Button
    btn = Button(tab, text="Set", command=clicked)
    btn.grid(column=2, row=0)

###############################################################################
def LA(tab,ruta):
    # Panel control
    param = LabelFrame(tab, text='Estado válvula')
    param.grid(row=0, column=0, padx=46, pady=30)
    
    # Button click function
    def clicked():
         # Reading current value from the file to modify 
        archivo = open(ruta,'r')
        estado = archivo.read()
        archivo.close()
        
        # convert string to float and the to bool
        is_on = bool(float(estado))
        
        if is_on:
            btn.config(text='OFF', bg='red', fg='black')
            lbl.config(text='Encender')
            contenido = '0'
        else:
            btn.config(text='ON', bg='green', fg='cyan')
            lbl.config(text='Apagar')
            contenido = '1'
            
        archivo = open(ruta,'w')
        archivo.write(contenido)
        archivo.close()
    
    # Reading current value from the file to modify    
    archivo = open(ruta,'r')
    estado = archivo.read()
    archivo.close()
    
    # convert string to float and the to bool
    is_on = bool(float(estado))
        
    if is_on:
        btn = Button(param, text="ON", command=clicked, bg='green', fg='cyan')
        lbl = Label(param, text="Apagar")
    else:
        btn = Button(param, text="OFF", command=clicked, bg='red', fg='black')
        lbl = Label(param, text="Encender")
    
    btn.grid(column=0, row=1, sticky=W, padx=26, pady=5)        
    lbl.grid(column=0, row=2, sticky=W, padx=18, pady=2)
    
###############################################################################    
def carga(archivo):
    p = np.zeros([6,1]) 
    i=0
    # Read line by line
    for linea in archivo.readlines():
        p[i] = linea
        i=i+1
    return p