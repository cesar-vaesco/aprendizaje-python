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


def evento1():
    boton1.config(text="Botón 1 presionado")


def evento2():
    boton2.config(text="Botón 2 presionado")


def evento3():
    boton3.config(text="Botón 3 presionado")


def evento4():
    boton4.config(
        text="Botón 4 presionado", fg="white", relief=tk.GROOVE, background="purple"
    )


ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Manejo de Grid")
ventana.iconbitmap("34-tkinter/icono.ico")

# Configurar el grid
ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=10)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

boton1 = ttk.Button(ventana, text="Botón 1", command=evento1)
boton1.grid(
    row=0,
    column=0,
    sticky="NSWE",
    pady=30,
    padx=40,
    ipady=50,
    ipadx=20,
    columnspan=2,
    rowspan=2,
)


# N(arriba),E(derecha),S(abajo),w(izquierda)
boton2 = ttk.Button(ventana, text="Botón 2", command=evento2)
# boton2.grid(row=1, column=0, sticky="NSWE")

boton3 = ttk.Button(ventana, text="Botón 3", command=evento3)
# boton3.grid(row=0, column=1, sticky="NSWE")

# N(arriba),E(derecha),S(abajo),w(izquierda)
boton4 = tk.Button(ventana, text="Botón 4", command=evento4)
# boton4.grid(row=1, column=1, sticky="NSWE")


center_window(ventana)

ventana.mainloop()
