import tkinter as tk
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


def enviar():
    # Modificamos el texto del label
    etiqueta1.config(text=entrada_var1.get())


ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Manejo de componentes tkinter")
ventana.iconbitmap("34-tkinter/icono.ico")


# Definimos una variable
entrada_var1 = tk.StringVar(value="Valor por dafault")
entrada1 = ttk.Entry(ventana, width=30, textvariable=entrada_var1)
entrada1.grid(row=0, column=0)

# Etiqueta (Label)
etiqueta1 = tk.Label(ventana, text="Aquí se mostrará el contenido de la caja de texto")
etiqueta1.grid(row=1, column=0, columnspan=2)

# Creamos un botón
boton1 = ttk.Button(ventana, text="Enviar", command=enviar)
boton1.grid(row=0, column=1)

center_window(ventana)

ventana.mainloop()
