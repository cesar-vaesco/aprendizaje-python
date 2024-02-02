# GUI Graphical user interface
# Tkinder TK Interface

import tkinter as Tk

# importamos módulo del trma de tkinter
from tkinter import ttk


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    frm_width = window.winfo_rootx() - window.winfo_x()
    win_width = width + 2 * frm_width
    height = window.winfo_height()
    titlebar_height = window.winfo_rooty() - window.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = window.winfo_screenwidth() // 2 - win_width // 2
    y = window.winfo_screenheight() // 2 - win_height // 2
    window.geometry("{}x{}+{}+{}".format(width, height, x, y))
    window.deiconify()


def evento_click():
    boton1.config(text="Botón presionado")
    print("Ejecución del evento_click ")
    # Crear un nuevo componente y lo mostramos
    boton2 = ttk.Button(ventana, text="Nuevo botón")
    boton2.pack()


# Usamos un objeto usando la clase tk
ventana = Tk.Tk()
# Modificamos el tamaño de la ventana
ventana.geometry("600x400")
# Cambiamos el nombre de la ventana
ventana.title("Nueva ventana")
# Configuramos el icono de la aplicación
ventana.iconbitmap("34-tkinter/icono.ico")
# Creamos un botón(widget), el objeto padre es la ventana
boton1 = ttk.Button(ventana, text="Dar click", command=evento_click)
# Utilizamos el pack layout manager para mostrar el botón de la ventana
boton1.pack()


# ventana.resizable(0, 0)
# Centrar la ventana.
center_window(ventana)

# El método mainloop() debe de ser declarado al final de nuestro código y sin el no se visualiza la ventana
ventana.mainloop()
