import tkinter as tk
import sys
from time import sleep

from tkinter import ttk, messagebox, scrolledtext


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


def crear_componentes_tabulador1(tabulador):
    # Agregar una etiqueta y un componente de entrada
    etiqueta1 = ttk.Label(tabulador, text="Nombre: ")
    etiqueta1.grid(row=0, column=0, sticky=tk.E)
    entrada1 = ttk.Entry(tabulador, width=30)
    entrada1.grid(row=0, column=1, padx=5, pady=5)

    def enviar():
        messagebox.showinfo("Mensaje", f"Nombre: {entrada1.get()}")

    # Agregamos un botón
    boton1 = ttk.Button(tabulador, text="Enviar", command=enviar)
    boton1.grid(row=1, column=0, columnspan=2)


def crear_componentes_tabulador2(tabulador):
    contenido = "Texto del contenido:  "
    # Creamos el conponente de scroll
    scroll = scrolledtext.ScrolledText(tabulador, width=50, height=10, wrap=tk.WORD)
    scroll.insert(tk.INSERT, contenido)
    # Mostramos el componente
    scroll.grid(row=0, column=0, padx=15, pady=10)


def crear_componentes_tabulador3(tabulador):
    # Crear lista unsado data list comprehencions
    datos = [x + 1 for x in range(10)]
    combobox = ttk.Combobox(tabulador, width=15, values=datos)
    combobox.grid(row=0, column=0, padx=10, pady=10)
    combobox.current(0)

    # Agregar un botón para saber que opción selecciono el usuario
    def mostrarvalor():
        messagebox.showinfo(
            "Valor seleccionado", f"Valor seleccionado: {combobox.get()}"
        )

    boton1 = ttk.Button(
        tabulador, text="Mostrar valor seleccionado:  ", command=mostrarvalor
    )
    boton1.grid(row=0, column=1)


def crear_componentes_tabulador4(tabulador):

    def mostrar_titulo():
        messagebox.showinfo(
            "Más info de la imagen: ", f"Nombre de imagen: {imagen.cget('file')}"
        )

    imagen = tk.PhotoImage(file="35-componentes/python-logo.png")
    boton_imagen = ttk.Button(tabulador, image=imagen, command=mostrar_titulo)
    boton_imagen.grid(row=0, column=0, padx=10, pady=10)


def crear_componentes_tabulador5(tabulador):

    def ejecutar_barra():
        barra_progreso["maximum"] = 100
        for valor in range(101):
            # Mandamos a esperar un poco antes de continuar con la ejecución de la barra
            sleep(0.085)  # import time
            # Incfrementamos nuestra barra de progreso
            barra_progreso["value"] = valor
            # Actualizamos barra progrso
            barra_progreso.update()
        barra_progreso["value"] = 0

    def ejecutar_ciclo():
        barra_progreso.start()

    def detener():
        barra_progreso.stop()

    def detener_despues():
        esperarms = 1800
        ventana.after(esperarms, barra_progreso.stop())

    # Compnente de barra de progreso
    barra_progreso = ttk.Progressbar(tabulador, orient="horizontal", length=550)
    barra_progreso.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

    # Botones para controlar los eventos de una barra de progreso
    boton_inicio = ttk.Button(
        tabulador, text="Ejecutar barra de progreso", command=ejecutar_barra
    )
    boton_inicio.grid(row=1, column=0)

    boton_ciclo = ttk.Button(tabulador, text="Ejecutar ciclo", command=ejecutar_ciclo)
    boton_ciclo.grid(row=1, column=1)

    boton_detener = ttk.Button(tabulador, text="Detener ejecución", command=detener)
    boton_detener.grid(row=1, column=2)

    boton_despues = ttk.Button(
        tabulador, text="Detener ejecución después...", command=detener_despues
    )
    boton_despues.grid(row=1, column=3)


def crear_componenetes_salir(tabulador):

    # Agregamos un botón
    boton1 = ttk.Button(tabulador, text="Salir....", command=salir)
    # Posicionamiento de botón
    boton1.place(relx=0.5, rely=0.5, width=100, anchor="c")


def salir():
    message_salida = "Saliendo de la aplicación..... "
    messagebox.showerror("Mensaje informatico: ", message_salida)
    ventana.quit()
    ventana.destroy()
    print(message_salida)
    sys.exit()


def crear_tabs():

    # Creamos un tab control, para elo usamos la clase Notebook
    control_tabulador = ttk.Notebook(ventana)
    # Agregamos un marco(frame)paa agregar dentro del tab y organizar
    tabulador1 = ttk.Frame(control_tabulador)

    # Primer tabulador -agregamos el tabulador al control de tabuladores
    control_tabulador.add(tabulador1, text="Tabulador 1")
    # Mostramos el tabulador
    control_tabulador.pack(fill="both")

    # Creamos segundo tabulador
    tabulador2 = ttk.LabelFrame(control_tabulador, text="Contenido")
    control_tabulador.add(tabulador2, text="Tabulador 2")

    # Crear un tercer tabulador
    tabulador3 = ttk.Frame(control_tabulador)
    control_tabulador.add(tabulador3, text="Tabulador 3")

    # Crear un cuarto tabulador
    tabulador4 = ttk.LabelFrame(control_tabulador, text="Imagen")
    control_tabulador.add(tabulador4, text="Tabulador 4")

    # Quinto tabulador
    tabulador5 = ttk.LabelFrame(control_tabulador, text="Barra de progreso")
    control_tabulador.add(tabulador5, text="Tabulador 5")

    # Creamos tabulador para agregar la opción salir
    salir = ttk.Frame(control_tabulador)
    control_tabulador.add(salir, text="Salir...")

    crear_componentes_tabulador1(tabulador1)
    crear_componentes_tabulador2(tabulador2)
    crear_componentes_tabulador3(tabulador3)
    crear_componentes_tabulador4(tabulador4)
    crear_componentes_tabulador5(tabulador5)
    crear_componenetes_salir(salir)


ventana = tk.Tk()
ventana.geometry("630x400")
ventana.title("Componentes")
ventana.iconbitmap("35-componentes/icono.ico")
centrar_ventana(ventana)

crear_tabs()

ventana.mainloop()
