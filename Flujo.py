import tkinter as tk


class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interfaz Gráfica")
        self.geometry("800x600")
        self.configure(bg='#dcdcdc')

        # Crear frames para los menús
        self.frames = {
            "menu_principal": tk.Frame(self, bg='#dcdcdc'),
            "submenu": tk.Frame(self, bg='#dcdcdc'),
            "menu": tk.Frame(self, bg='#dcdcdc'),
            "configuracion": tk.Frame(self, bg='#dcdcdc')
        }

        for frame in self.frames.values():
            frame.pack(side=tk.TOP, fill=tk.X)

        # Inicializar el botón seleccionado
        self.boton_seleccionado_principal = None
        self.boton_seleccionado_spei = None
        self.boton_seleccionado_cuentas = None
        self.boton_seleccionado_varios = None

        # Agregar opciones al menú principal como botones
        self.crear_menu_principal()

    def crear_menu_principal(self):
        opciones_menu_principal = ["Spei", "STP", "Administración"]
        for opcion in opciones_menu_principal:
            btn = self.crear_boton(
                self.frames["menu_principal"], opcion, self.mostrar_opciones_menu_principal)
            btn.pack(side=tk.LEFT, padx=2, pady=1)

    def crear_boton(self, frame, texto, comando):
        """Crea un botón con estilo y configuración específica."""
        btn = tk.Button(frame, text=texto, bg='#d0cdc4',
                        fg='#8f7768', width=25)
        btn.config(command=lambda: comando(texto, btn))
        return btn

    def mostrar_opciones_menu_principal(self, opcion, boton):
        # Cambiar el color del botón seleccionado en el menú principal
        if self.boton_seleccionado_principal:
            self.boton_seleccionado_principal.config(bg='#d0cdc4')

        boton.config(bg='#b9b1ad')
        self.boton_seleccionado_principal = boton

        # Limpiar todo el submenú y el menú
        self.limpiar_submenu()
        self.limpiar_menu()
        self.limpiar_configuracion()

        if opcion == "Spei":
            self.mostrar_opciones_spei()
        else:
            self.mostrar_mensaje(opcion)

    def limpiar_submenu(self):
        """Limpia el frame de submenú."""
        for widget in self.frames["submenu"].winfo_children():
            widget.destroy()

    def limpiar_menu(self):
        """Limpia el frame de menú."""
        for widget in self.frames["menu"].winfo_children():
            widget.destroy()

        # Reiniciar las variables de botones seleccionados en el menú
        self.boton_seleccionado_cuentas = None
        self.boton_seleccionado_varios = None
        self.boton_seleccionado_spei = None  # Reiniciar el botón de Spei

    def limpiar_configuracion(self):
        """Limpia el frame de configuración."""
        for widget in self.frames["configuracion"].winfo_children():
            widget.destroy()

        # Reiniciar las variables de botones seleccionados en configuración
        self.boton_seleccionado_varios = None

    def mostrar_opciones_spei(self):
        # Opciones del menú "Spei"
        opciones_spei = ["Recepción de Órdenes", "Cuentas",
                         "Catálogos", "Varios/Administración"]
        for opcion in opciones_spei:
            btn = self.crear_boton(
                self.frames["submenu"], opcion, self.mostrar_opciones_spei_seleccionada)
            btn.pack(side=tk.LEFT, padx=2, pady=1)

    def mostrar_opciones_spei_seleccionada(self, opcion, boton):
        # Cambiar el color del botón seleccionado en el menú de Spei
        if self.boton_seleccionado_spei:
            self.boton_seleccionado_spei.config(bg='#d0cdc4')

        boton.config(bg='#b9b1ad')
        self.boton_seleccionado_spei = boton

        # Limpiar solo el frame de menú
        self.limpiar_menu()

        if opcion == "Recepción de Órdenes":
            self.mostrar_recepcion_ordenes()
        elif opcion == "Cuentas":
            self.mostrar_cuentas()
        elif opcion == "Catálogos":
            self.mostrar_catalogos()
        elif opcion == "Varios/Administración":
            self.mostrar_varios_administracion()

    def mostrar_recepcion_ordenes(self):
        print("Mostrando la recepción de órdenes...")

    def mostrar_cuentas(self):
        # Opciones del menú "Cuentas"
        opciones_cuentas = ["Saldo", "Manto. Cuentas",
                            "Manto. Empresas", "Configuración Empresas"]
        for opcion in opciones_cuentas:
            btn = self.crear_boton(
                self.frames["menu"], opcion, self.mostrar_opciones_cuentas_seleccionada)
            btn.pack(side=tk.LEFT, padx=2, pady=1)

    def mostrar_opciones_cuentas_seleccionada(self, opcion, boton):
        # Cambiar el color del botón seleccionado en el menú de cuentas
        if self.boton_seleccionado_cuentas:
            self.boton_seleccionado_cuentas.config(bg='#d0cdc4')

        boton.config(bg='#b9b1ad')
        self.boton_seleccionado_cuentas = boton

        # Limpiar solo el frame de configuración antes de agregar nuevas opciones
        self.limpiar_configuracion()

        # Mostrar las opciones del menú seleccionado
        if opcion == "Saldo":
            self.mostrar_saldo()
        elif opcion == "Manto. Cuentas":
            self.mostrar_manto_cuentas()
        elif opcion == "Manto. Empresas":
            self.mostrar_manto_empresas()
        elif opcion == "Configuración Empresas":
            self.mostrar_opciones_configuracion_empresas()

    def mostrar_saldo(self):
        print("Mostrando el saldo actual...")

    def mostrar_manto_cuentas(self):
        # Opciones del menú "Manto. Cuentas"
        opciones_manto_cuentas = ["Propias",
                                  "Terceros", "Manto. Cuenta Terceros"]
        for opcion in opciones_manto_cuentas:
            btn = self.crear_boton(
                self.frames["configuracion"], opcion, self.mostrar_mensaje)
            btn.pack(side=tk.LEFT, padx=2, pady=1)

    def mostrar_manto_empresas(self):
        print("Mostrando mantenimiento de empresas...")

    def mostrar_opciones_configuracion_empresas(self):
        opciones_configuracion = ["Generales", "Traspasos", "Tarjeta Débito"]
        for opcion in opciones_configuracion:
            btn = self.crear_boton(
                self.frames["configuracion"], opcion, self.mostrar_mensaje)
            btn.pack(side=tk.LEFT, padx=2, pady=1)

    def mostrar_catalogos(self):
        print("Mostrando los catálogos...")

    def mostrar_varios_administracion(self):
        # Opciones del menú "Varios/Administración"
        opciones_varios = ["Archivos", "Configuración", "Folio Solicitud CEP"]
        for opcion in opciones_varios:
            btn = self.crear_boton(
                self.frames["menu"], opcion, self.mostrar_opciones_varios_seleccionada)
            btn.pack(side=tk.LEFT, padx=2, pady=1)

    def mostrar_opciones_varios_seleccionada(self, opcion, boton):
        # Cambiar el color del botón seleccionado en el menú de varios
        if self.boton_seleccionado_varios:
            self.boton_seleccionado_varios.config(bg='#d0cdc4')

        boton.config(bg='#b9b1ad')
        self.boton_seleccionado_varios = boton

        # Limpiar solo el frame de configuración antes de agregar nuevas opciones
        self.limpiar_configuracion()

        if opcion == "Archivos":
            self.mostrar_mensaje("Archivos seleccionada")
        elif opcion == "Configuración":
            self.mostrar_configuracion_varios()
        elif opcion == "Folio Solicitud CEP":
            self.mostrar_mensaje("Folio Solicitud CEP seleccionada")

    def mostrar_configuracion_varios(self):
        opciones_configuracion = [
            "Procesos Automáticos", "Mensajes H2H", "Generales", "CEP"]
        for opcion in opciones_configuracion:
            btn = self.crear_boton(
                self.frames["configuracion"], opcion, self.mostrar_mensaje)
            btn.pack(side=tk.LEFT, padx=2, pady=1)

    def mostrar_mensaje(self, opcion):
        print(f"{opcion} seleccionada")


# Ejecutar la aplicación
if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
