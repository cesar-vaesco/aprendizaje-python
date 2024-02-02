import tkinter as tk
from tkinter import ttk, messagebox


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
    etiqueta1.config(text=entrada1.get())
    #  Messagebox
    mensaje1 = entrada1.get()

    # Para poder mostrar los tres mensajes al mismo tiempo
    if mensaje1:
        messagebox.showinfo("Mensaje informativo: ", mensaje1 + " Informativo")
        messagebox.showwarning("Mensaje de alerta: ", mensaje1 + " !Alerta¡")
        messagebox.showerror("Mensaje de error: ", mensaje1 + " !!!!Error¡¡¡¡")
    elif not mensaje1:
        mensaje1 = " CIERRE DE VENTANA "
        messagebox.showerror(
            "¡¡¡¡NO HAY DATOS!!!!",
            mensaje1 + " !!!!Error¡¡¡¡ ",
        )


ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Manejo de componentes tkinter")
ventana.iconbitmap("34-tkinter/icono.ico")


entrada1 = ttk.Entry(ventana, width=30)
entrada1.grid(row=0, column=0)

# Etiqueta (Label)
etiqueta1 = tk.Label(ventana, text="Aquí se mostrará el contenido de la caja de texto")
etiqueta1.grid(row=1, column=0, columnspan=2)

# Creamos un botón
boton1 = ttk.Button(ventana, text="Enviar", command=enviar)
boton1.grid(row=0, column=1)

center_window(ventana)

ventana.mainloop()
