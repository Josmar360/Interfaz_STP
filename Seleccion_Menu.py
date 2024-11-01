import tkinter as tk


class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interfaz Gráfica")
        self.geometry("800x600")

        # Establecer el color de fondo de la aplicación
        self.configure(bg='#dcdcdc')

        # Crear el frame para las opciones del menú principal
        self.frame_menu_principal = tk.Frame(self, bg='#dcdcdc')
        self.frame_menu_principal.pack(side=tk.TOP, fill=tk.X)

        # Crear el frame para las opciones de segundo nivel
        self.frame_submenu = tk.Frame(self, bg='#dcdcdc')
        self.frame_submenu.pack(side=tk.TOP, fill=tk.X)

        # Crear el frame para las opciones de tercer nivel
        self.frame_menu = tk.Frame(self, bg='#dcdcdc')
        self.frame_menu.pack(side=tk.TOP, fill=tk.X)

        # Crear el frame para las opciones de cuarto nivel
        self.frame_configuracion = tk.Frame(self, bg='#dcdcdc')
        self.frame_configuracion.pack(side=tk.TOP, fill=tk.X)

        # Inicializar el botón seleccionado
        self.boton_seleccionado_principal = None
        self.boton_seleccionado_spei = None
        self.boton_seleccionado_cuentas = None

        # Agregar opciones al menú principal como botones
        self.crear_menu_principal()

    def crear_menu_principal(self):
        # Opciones del menú principal
        opciones_menu_principal = ["Spei", "STP", "Administración"]
        for opcion in opciones_menu_principal:
            btn = tk.Button(
                self.frame_menu_principal,
                text=opcion,
                bg='#d0cdc4',  # Color de fondo del botón
                fg='#8f7768',  # Color del texto
                width=25
            )
            btn.config(command=lambda opt=opcion,
                       b=btn: self.mostrar_opciones_menu_principal(opt, b))
            btn.pack(side=tk.LEFT, padx=2, pady=1)

    def mostrar_opciones_menu_principal(self, opcion, boton):
        # Restablecer el color del botón anterior en el menú principal
        if self.boton_seleccionado_principal:
            self.boton_seleccionado_principal.config(
                bg='#d0cdc4')  # Color original

        # Cambiar el color del botón seleccionado en el menú principal
        boton.config(bg='#b9b1ad')  # Color más oscuro
        self.boton_seleccionado_principal = boton  # Guardar el botón seleccionado

        # Limpiar o ocultar los menús de segundo, tercer y cuarto nivel
        for widget in self.frame_submenu.winfo_children():
            widget.destroy()  # Limpiar el frame de submenú
        for widget in self.frame_menu.winfo_children():
            widget.destroy()  # Limpiar el frame de menú
        for widget in self.frame_configuracion.winfo_children():
            widget.destroy()  # Limpiar el frame de configuración

        if opcion == "Spei":
            self.mostrar_opciones_spei()
        else:
            self.mostrar_mensaje(opcion)

    def mostrar_opciones_spei(self):
        # Limpiar el frame de submenú antes de agregar nuevas opciones
        for widget in self.frame_submenu.winfo_children():
            widget.destroy()

        # Opciones del menú "Spei"
        opciones_spei = ["Recepción de Órdenes", "Cuentas",
                         "Catálogos", "Varios/Administración"]
        for opcion in opciones_spei:
            btn = tk.Button(
                self.frame_submenu,
                text=opcion,
                bg='#d0cdc4',  # Color de fondo del botón
                fg='#8f7768',  # Color del texto
                width=25
            )
            btn.config(command=lambda opt=opcion,
                       b=btn: self.mostrar_opciones_detalle_spei(opt, b))
            btn.pack(side=tk.LEFT, padx=2, pady=1)

    def mostrar_opciones_detalle_spei(self, opcion, boton):
        # Limpiar el frame de menú antes de agregar nuevas opciones
        for widget in self.frame_menu.winfo_children():
            widget.destroy()

        # Restablecer el color del botón anterior en el menú de Spei
        if self.boton_seleccionado_spei:
            self.boton_seleccionado_spei.config(bg='#d0cdc4')  # Color original

        # Cambiar el color del botón seleccionado en el menú de Spei
        boton.config(bg='#b9b1ad')  # Color más oscuro
        self.boton_seleccionado_spei = boton  # Guardar el botón seleccionado

        # Mostrar las opciones del menú seleccionado
        if opcion == "Cuentas":
            self.mostrar_opciones_cuentas()
        else:
            self.mostrar_mensaje(opcion)

    def mostrar_opciones_cuentas(self):
        # Opciones del menú "Cuentas"
        opciones_cuentas = ["Saldo", "Manto. Cuentas",
                            "Manto. Empresas", "Configuración Empresas"]
        for opcion in opciones_cuentas:
            btn = tk.Button(
                self.frame_menu,
                text=opcion,
                bg='#d0cdc4',  # Color de fondo del botón
                fg='#8f7768',  # Color del texto
                width=25
            )
            btn.config(command=lambda opt=opcion,
                       b=btn: self.mostrar_opciones_configuracion_empresas(opt, b))
            btn.pack(side=tk.LEFT, padx=2, pady=1)

    def mostrar_opciones_configuracion_empresas(self, opcion, boton):
        # Limpiar el frame de configuración antes de agregar nuevas opciones
        for widget in self.frame_configuracion.winfo_children():
            widget.destroy()

        # Restablecer el color del botón anterior en el menú de Cuentas
        if self.boton_seleccionado_cuentas:
            self.boton_seleccionado_cuentas.config(
                bg='#d0cdc4')  # Color original

        # Cambiar el color del botón seleccionado en el menú de Cuentas
        boton.config(bg='#b9b1ad')  # Color más oscuro
        self.boton_seleccionado_cuentas = boton  # Guardar el botón seleccionado

        # Limpiar el menú de configuración anterior si existe
        for widget in self.frame_configuracion.winfo_children():
            widget.destroy()

        # Mostrar las opciones del menú "Configuración Empresas"
        opciones_configuracion = ["Generales", "Traspasos", "Tarjeta Débito"]
        for opcion in opciones_configuracion:
            btn = tk.Button(
                self.frame_configuracion,
                text=opcion,
                bg='#d0cdc4',  # Color de fondo del botón
                fg='#8f7768',  # Color del texto
                width=25
            )
            btn.config(command=lambda opt=opcion: self.mostrar_mensaje(opt))
            btn.pack(side=tk.LEFT, padx=2, pady=1)

    def mostrar_mensaje(self, opcion):
        print(f"{opcion} seleccionada")


# Ejecutar la aplicación
if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
