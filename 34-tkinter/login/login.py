import sys
import tkinter as tk
from tkinter import END, ttk, messagebox


# Centrar ventana
def centrar_ventana(ventana):
    ventana.update_idletasks()
    width = ventana.winfo_width()
    frm_width = ventana.winfo_rootx() - ventana.winfo_x()
    win_width = width + 2 * frm_width
    height = ventana.winfo_height()
    titlebar_height = ventana.winfo_rooty() - ventana.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = ventana.winfo_screenwidth() // 2 - win_width // 2
    y = ventana.winfo_screenheight() // 2 - win_height // 2
    ventana.geometry("{}x{}+{}+{}".format(width, height, x, y))
    ventana.deiconify()


# ventana principal
ventana = tk.Tk()
ventana.geometry("300x130")
ventana.title("Login")
ventana.iconbitmap("34-tkinter/login/login.ico")
ventana.resizable(0, 0)

# configuración del grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=3)

# usuario
usuario_etiqueta = ttk.Label(ventana, text="Usuario:")
usuario_etiqueta.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
usuario_entrada = ttk.Entry(ventana)
usuario_entrada.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

# password
password_etiqueta = ttk.Label(ventana, text="Password:")
password_etiqueta.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
password_entrada = ttk.Entry(ventana, show="*")
password_entrada.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)


def limpiar_texto_Entry():
    usuario_entrada.delete(0, END)
    password_entrada.delete(0, END)


# boton Login
def login():

    if usuario_entrada.get():
        if password_entrada.get():
            messagebox.showinfo(
                "Datos Login",
                f"usuario: {usuario_entrada.get()}, Password: {password_entrada.get()}",
            )

    if not password_entrada.get():
        mensaje1 = " Password con datos vacíos"
        messagebox.showerror("¡¡¡¡NO HAY DATOS!!!!", mensaje1 + " !!!!Error¡¡¡¡ ")

    if not usuario_entrada.get():
        mensaje1 = " Usuario con datos vacíos"
        messagebox.showerror("¡¡¡¡NO HAY DATOS!!!!", mensaje1 + " !!!!Error¡¡¡¡ ")

    limpiar_texto_Entry()


def salir():
    message_salida = "Saliendo de la aplicación..... "
    messagebox.showerror("Mensaje informatico: ", message_salida)
    ventana.quit()
    ventana.destroy()
    print(message_salida)
    sys.exit()


login_boton = ttk.Button(ventana, text="Login", command=login)
# login_boton.grid(row=3, column=0, columnspan=2)
login_boton.grid(row=5, column=0, padx=20, pady=20)

salir_boton = ttk.Button(ventana, text="Salir", command=salir)
salir_boton.grid(row=5, column=2, padx=20, pady=20)

centrar_ventana(ventana)

# Ejecutar la ventana
ventana.mainloop()
