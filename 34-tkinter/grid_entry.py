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


ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Entry data tkinter")
ventana.iconbitmap("34-tkinter/icono.ico")


#  width es la cantidad de caracteres que ocupa la caja
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER)
entrada1.grid(row=0, column=0)
#  Insert agrega un texto a nuestra caja de texto
#  Texto de guía para introducir datos en la caja de texto
entrada1.insert(0, "Introduce una cadena")
entrada1.insert(tk.END, ":  ")

center_window(ventana)

ventana.mainloop()
