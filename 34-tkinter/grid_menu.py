import sys
import tkinter as tk
from tkinter import Menu, ttk, messagebox


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
    mensaje1 = entrada1.get()
    if mensaje1:
        messagebox.showinfo("Mensaje informativo: ", mensaje1 + " Informativo")
    elif not mensaje1:
        mensaje1 = " CIERRE DE VENTANA "
        messagebox.showerror(
            "¡¡¡¡NO HAY DATOS!!!!",
            mensaje1 + " !!!!Error¡¡¡¡ ",
        )


def nuevo():
    messagebox.showinfo("Mensaje informativo: ", "Pulso la opción nuevo")


def acerca_de():
    messagebox.showwarning(
        "Mensaje informativo: ", "Por el momento no hay apoyo técnico"
    )


def salir():
    message_salida = "Saliendo de la aplicación..... "
    messagebox.showerror("Mensaje informatico: ", message_salida)
    ventana.quit()
    ventana.destroy()
    print(message_salida)
    sys.exit()


def crear_menu():
    # Configurar el menú principal
    menu_principal = Menu(ventana)
    # tearoff = False para evitar que se separa el menú de la interfaz
    submenu_archivo = Menu(menu_principal, tearoff=False)
    # Agregamos una nueva opción al menu de archivo
    submenu_archivo.add_command(label="Nuevo", command=nuevo)
    # Agregar un separador
    submenu_archivo.add_separator()
    # Opción de salir
    submenu_archivo.add_command(label="Salir", command=salir)
    # Agregamos el submenu al menu principal
    menu_principal.add_cascade(menu=submenu_archivo, label="Archivo")
    # Submenú de ayuda
    submenu_ayuda = Menu(menu_principal, tearoff=0)
    # Submenu acerca de
    submenu_ayuda.add_command(label="Acerca de", command=acerca_de)
    # Agregar al menú el nuevo submenu
    menu_principal.add_cascade(menu=submenu_ayuda, label="Ayuda")
    # Mostrar menú en la ventana principal
    ventana.config(menu=menu_principal)


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

crear_menu()

center_window(ventana)

ventana.mainloop()
