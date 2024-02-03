import sys
import tkinter as tk
from tkinter import END, ttk, messagebox


class LoginVentana(tk.Tk):
    def __init__(self):
        super().__init__()
        # ventana principal
        self.geometry("300x130")
        self.title("Login")
        self.iconbitmap("34-tkinter/login/login.ico")
        self.resizable(0, 0)
        # configuración del grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        # Creamos los componentes
        self._crear_componentes()
        self._centrar_ventana()

    # Definir el método crear_componentes
    def _crear_componentes(self):
        # usuario
        usuario_etiqueta = ttk.Label(self, text="Usuario:")
        usuario_etiqueta.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.usuario_entrada = ttk.Entry(self)
        self.usuario_entrada.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        # password
        password_etiqueta = ttk.Label(self, text="Password:")
        password_etiqueta.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self.password_entrada = ttk.Entry(self, show="*")
        self.password_entrada.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        # boton Login
        login_boton = ttk.Button(self, text="Login", command=self._login)
        login_boton.grid(row=5, column=0, padx=20, pady=20)
        # botón Salir
        salir_boton = ttk.Button(self, text="Salir", command=self._salir)
        salir_boton.grid(row=5, column=2, padx=20, pady=20)

    # Centrar ventana
    def _centrar_ventana(self):
        self.update_idletasks()
        width = self.winfo_width()
        frm_width = self.winfo_rootx() - self.winfo_x()
        win_width = width + 2 * frm_width
        height = self.winfo_height()
        titlebar_height = self.winfo_rooty() - self.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.winfo_screenwidth() // 2 - win_width // 2
        y = self.winfo_screenheight() // 2 - win_height // 2
        self.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.deiconify()

    # Limpiar texto
    def _limpiar_texto_entry(self):
        self.usuario_entrada.delete(0, END)
        self.password_entrada.delete(0, END)

    # Acción salir
    def _salir(self):
        message_salida = "Saliendo de la aplicación..... "
        messagebox.showerror("Mensaje informatico: ", message_salida)
        self.quit()
        self.destroy()
        print(message_salida)
        sys.exit()

    def _login(self):
        if self.usuario_entrada.get():
            if self.password_entrada.get():
                messagebox.showinfo(
                    "Datos Login",
                    f"usuario: {self.usuario_entrada.get()}, Password: {self.password_entrada.get()}",
                )

        if not self.password_entrada.get():
            mensaje1 = " Password con datos vacíos"
            messagebox.showerror("¡¡¡¡NO HAY DATOS!!!!", mensaje1 + " !!!!Error¡¡¡¡ ")

        if not self.usuario_entrada.get():
            mensaje1 = " Usuario con datos vacíos"
            messagebox.showerror("¡¡¡¡NO HAY DATOS!!!!", mensaje1 + " !!!!Error¡¡¡¡ ")

        self._limpiar_texto_entry()


# Ejecutar la ventana
if __name__ == "__main__":
    login_ventana = LoginVentana()
    login_ventana.mainloop()
