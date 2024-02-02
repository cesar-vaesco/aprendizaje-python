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
    print(entrada1.get())
    boton1.config(text=entrada1.get())
    # Elimknar el contenido
    # entrada1.delete(0, tk.END)
    # Seleccionar el texto de la caja
    entrada1.select_range(0, tk.END)
    # Para hacer efectiva la selección
    entrada1.focus()


ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Entry data tkinter")
ventana.iconbitmap("34-tkinter/icono.ico")


#  width es la cantidad de caracteres que ocupa la caja
# entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, show="*")
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER)
entrada1.grid(row=0, column=0)
#  Insert agrega un texto a nuestra caja de texto
#  Texto de guía para introducir datos en la caja de texto
entrada1.insert(0, "Introduce una cadena")
entrada1.insert(tk.END, ":  ")
# entrada1.config(state="readonly")

# Creamos un botón
boton1 = ttk.Button(ventana, text="Enviar", command=enviar)
boton1.grid(row=0, column=1)

center_window(ventana)

ventana.mainloop()
