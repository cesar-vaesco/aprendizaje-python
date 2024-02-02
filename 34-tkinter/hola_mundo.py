# GUI Graphical user interface
# Tkinder TK Interface

import tkinter as Tk


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


# Usamos un objeto usando la clase tk
ventana = Tk.Tk()
# Modificamos el tamaño de la ventana
ventana.geometry("600x400")
# Cambiamos el nombre de la ventana
ventana.title("Nueva ventana")
# ventana.resizable(0, 0)
# Centrar la ventana.
center_window(ventana)

# El método mainloop() debe de ser declarado al final de nuestro código y sin el no se visualiza la ventana
ventana.mainloop()
