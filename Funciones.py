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


# Primer nivel


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
           # Ajustar el comando dependiendo de la opción
            if opcion == "Recepción de Órdenes":
                btn.config(command=lambda opt=opcion,
                           # Llama a la función mostrar_recepcion_ordenes
                           b=btn: self.mostrar_recepcion_ordenes(opt, b))
            elif opcion == "Cuentas":
                btn.config(command=lambda opt=opcion,
                           # Llama a la función mostrar_recepcion_cuenta
                           b=btn: self.mostrar_cuentas(opt, b))
            elif opcion == "Catálogos":
                btn.config(command=lambda opt=opcion,
                           b=btn: self.mostrar_catalogos(opt, b))
            elif opcion == "Varios/Administración":
                btn.config(command=lambda opt=opcion,
                           # Llama a la función mostrar_opciones_configuracion_empresas
                           b=btn: self.mostrar_varios_admistracion(opt, b))
            btn.pack(side=tk.LEFT, padx=2, pady=1)


# Segundo nivel recepcion de ordenes


    def mostrar_recepcion_ordenes(self, opcion, boton):
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
        if opcion == "Recepción de Órdenes":
            self.mostrar_detalles_recepcion_ordenes()
        else:
            self.mostrar_mensaje(opcion)

    def mostrar_detalles_recepcion_ordenes(self):
        # Lógica para mostrar ordenes
        print("Mostrando el recepcion de ordenes....")

    def mostrar_cuentas(self, opcion, boton):
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
            self.mostrar_detalles_cuentas()
        else:
            self.mostrar_mensaje(opcion)

    def mostrar_detalles_cuentas(self):
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
            # Ajustar el comando dependiendo de la opción
            if opcion == "Saldo":
                btn.config(command=lambda opt=opcion,
                           # Llama a la función mostrar_saldo
                           b=btn: self.mostrar_saldo(opt, b))
            elif opcion == "Manto. Cuentas":
                btn.config(command=lambda opt=opcion,
                           # Llama a la función mostrar_manto_cuentas
                           b=btn: self.mostrar_manto_cuentas(opt, b))
            elif opcion == "Manto. Empresas":
                btn.config(command=lambda opt=opcion,
                           # Llama a la función mostrar_manto_empresas
                           b=btn: self.mostrar_manto_empresas(opt, b))
            elif opcion == "Configuración Empresas":
                btn.config(command=lambda opt=opcion,
                           # Llama a la función mostrar_opciones_configuracion_empresas
                           b=btn: self.mostrar_opciones_configuracion_empresas(opt, b))
            btn.pack(side=tk.LEFT, padx=2, pady=1)

    def mostrar_catalogos(self, opcion, boton):
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
        if opcion == "Catálogos":
            self.mostrar_detalles_catalogos()
        else:
            self.mostrar_mensaje(opcion)

    def mostrar_detalles_catalogos(self):
        # Limpiar el frame de configuración antes de agregar nuevas opciones
        #for widget in self.frame_configuracion.winfo_children():
            #widget.destroy()
        print("Mostrando los catalogos....")

    def mostrar_varios_admistracion(self, opcion, boton):
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
        if opcion == "Varios/Administración":
            self.mostrar_detalles_varios_admistracion()
        else:
            self.mostrar_mensaje(opcion)

    def mostrar_detalles_varios_admistracion(self):
        # Opciones del menú "Varios/Administracion"
        opciones_cuentas = ["Procesos Automaticos", "Mensajes H2H",
                            "Generales", "CEP"]
        for opcion in opciones_cuentas:
            btn = tk.Button(
                self.frame_menu,
                text=opcion,
                bg='#d0cdc4',  # Color de fondo del botón
                fg='#8f7768',  # Color del texto
                width=25
            )
            # Ajustar el comando dependiendo de la opción
            if opcion == "Procesos Automaticos":
                btn.config(command=lambda opt=opcion,
                           # Llama a la función mostrar_saldo
                           b=btn: self.mostrar_procesos_automaticos(opt, b))
            elif opcion == "Mensajes H2H":
                btn.config(command=lambda opt=opcion,
                           # Llama a la función mostrar_manto_cuentas
                           b=btn: self.mostrar_mensajes_h2h(opt, b))
            elif opcion == "Generales":
                btn.config(command=lambda opt=opcion,
                           # Llama a la función mostrar_manto_empresas
                           b=btn: self.mostrar_generales(opt, b))
            elif opcion == "CEP":
                btn.config(command=lambda opt=opcion,
                           # Llama a la función mostrar_opciones_configuracion_empresas
                           b=btn: self.mostrar_cep(opt, b))
            btn.pack(side=tk.LEFT, padx=2, pady=1)

# Tercer nivel

    def mostrar_saldo(self, opcion, boton):
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

        print("Mostrando el saldo actual...")  # Lógica para mostrar el saldo

    def mostrar_manto_cuentas(self, opcion, boton):
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
        opciones_configuracion = ["Propias",
                                  "Terceros", "Manto. Cuenta Terceros"]
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

    def mostrar_manto_empresas(self, opcion, boton):
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

        # Lógica para mantenimiento de empresas
        print("Mostrando mantenimiento de empresas...")


# Cuarto nivel

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

    def mostrar_procesos_automaticos(self, opcion, boton):
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

        # Lógica para mostrar el saldo
        print("Mostrando procesos automaticos...")

    def mostrar_mensajes_h2h(self, opcion, boton):
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

        # Lógica para mostrar el saldo
        print("Mostrando mensajes H2H...")

    def mostrar_generales(self, opcion, boton):
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

        # Lógica para mostrar el saldo
        print("Mostrando generales...")

    def mostrar_cep(self, opcion, boton):
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

        # Lógica para mostrar el saldo
        print("Mostrando CEP...")

# Mostrar mensaje de niveles

    def mostrar_mensaje(self, opcion):
        print(f"{opcion} seleccionada")


# Ejecutar la aplicación
if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
