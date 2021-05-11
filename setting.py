# -*- coding: utf-8 -*-
"""
Created on Thu May  6 19:34:27 2021

@author: Juanchi
"""

from tkinter import *
from tkinter import ttk
from fun_setting import *

window = Tk()

window.title("Configuración de parámetros")
window.geometry('190x205')

####---- Control de pestañas ---########
tab_control = ttk.Notebook(window)          # First, we create a tab control using Notebook class

######### Pestaña MPC_INTA #############
tab1 = ttk.Frame(tab_control)               # Create a tab using Frame class.
tab_control.add(tab1, text='MPC_INTA')      # Add that tab to the tab control.

ruta_inta = "C:/Users/Juanchi/Documents/MPC_INTA.txt"     # path to the file to modify
MPC_INTA(tab1,ruta_inta)                                # widgets in current tab

########### Pestaña MPC ###############
tab2 = ttk.Frame(tab_control) 
tab_control.add(tab2, text='MPC')

ruta = "C:/Users/Juanchi/Documents/MPC.txt"
MPC_INTA(tab2,ruta)

############ Pestaña PID ###############
tab3 = ttk.Frame(tab_control) 
tab_control.add(tab3, text='PID')

ruta_pid = "C:/Users/Juanchi/Documents/PID.txt"
PID(tab3,ruta_pid)

######### Pestaña lazo abierto ###########
tab = ttk.Frame(tab_control) 
tab_control.add(tab, text='LA')

ruta_la = "C:/Users/Juanchi/Documents/LA.txt"
LA(tab,ruta_la)

##########################################
tab_control.pack(expand=1, fill='both')     # Pack the tab control so it becomes visible in the window.

window.mainloop()