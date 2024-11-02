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
        self.boton_seleccionado_configuracion = None

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
        btn.config(command=lambda t=texto,
                   b=btn: comando(t, b))  # Cambiado aquí
        return btn

    def mostrar_opciones_menu_principal(self, opcion, boton):
        # Cambiar el color del botón seleccionado en el menú principal
        if self.boton_seleccionado_principal:
            self.boton_seleccionado_principal.config(bg='#d0cdc4')

        boton.config(bg='#b9b1ad')
        self.boton_seleccionado_principal = boton

        # Limpiar todos los menús y submenús antes de mostrar nuevas opciones
        self.limpiar_todo()

        if opcion == "Spei":
            self.mostrar_opciones_spei()
        else:
            self.mostrar_mensaje(opcion)

    def limpiar_todo(self):
        """Limpia todos los menús y submenús."""
        self.limpiar_submenu()
        self.limpiar_menu()
        self.limpiar_configuracion()

    def limpiar_submenu(self):
        """Limpia el frame de submenú sin afectar el menú principal."""
        for widget in self.frames["submenu"].winfo_children():
            widget.destroy()

    def limpiar_menu(self):
        """Limpia el frame de menú sin afectar el menú principal ni el submenú."""
        for widget in self.frames["menu"].winfo_children():
            widget.destroy()
        self.boton_seleccionado_cuentas = None  # Reinicia la variable

    def limpiar_configuracion(self):
        """Limpia el frame de configuración sin afectar otros menús."""
        for widget in self.frames["configuracion"].winfo_children():
            widget.destroy()
        self.boton_seleccionado_configuracion = None  # Reinicia la variable

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
            # Solo cambiar el color si el botón seleccionado aún existe
            try:
                self.boton_seleccionado_spei.config(bg='#d0cdc4')
            except tk.TclError:
                pass  # El botón ya no existe

        boton.config(bg='#b9b1ad')
        self.boton_seleccionado_spei = boton

        # Limpiar el menú y configuración antes de mostrar nuevas opciones
        self.limpiar_menu()
        self.limpiar_configuracion()  # Asegúrate de limpiar la configuración

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
            # Solo cambiar el color si el botón seleccionado aún existe
            try:
                self.boton_seleccionado_cuentas.config(bg='#d0cdc4')
            except tk.TclError:
                pass  # El botón ya no existe

        boton.config(bg='#b9b1ad')
        self.boton_seleccionado_cuentas = boton

        # Limpiar la configuración antes de mostrar nuevas opciones
        self.limpiar_configuracion()

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
                self.frames["configuracion"], opcion, self.mostrar_opciones_manto_cuentas_seleccionada)
            btn.pack(side=tk.LEFT, padx=2, pady=1)

    def mostrar_opciones_manto_cuentas_seleccionada(self, opcion, boton):
        # Cambiar el color del botón seleccionado en el menú de Manto. Cuentas
        if self.boton_seleccionado_configuracion:
            # Solo cambiar el color si el botón seleccionado aún existe
            try:
                self.boton_seleccionado_configuracion.config(bg='#d0cdc4')
            except tk.TclError:
                pass  # El botón ya no existe

        boton.config(bg='#b9b1ad')
        self.boton_seleccionado_configuracion = boton

        # Mostrar el mensaje y limpiar el menú
        self.mostrar_mensaje(opcion)

    def mostrar_manto_empresas(self):
        print("Mostrando mantenimiento de empresas...")

    def mostrar_opciones_configuracion_empresas(self):
        opciones_configuracion = ["Generales", "Traspasos", "Tarjeta Débito"]
        for opcion in opciones_configuracion:
            btn = self.crear_boton(
                self.frames["configuracion"], opcion, self.mostrar_opciones_configuracion_empresas_seleccionada)
            btn.pack(side=tk.LEFT, padx=2, pady=1)

    def mostrar_opciones_configuracion_empresas_seleccionada(self, opcion, boton):
        self.mostrar_mensaje(opcion)

    def mostrar_catalogos(self):
        print("Mostrando los catálogos...")

    def mostrar_varios_administracion(self):
        opciones_varios = ["Archivos", "Configuración", "Folio Solicitud CEP"]
        for opcion in opciones_varios:
            btn = self.crear_boton(
                self.frames["menu"], opcion, self.mostrar_opciones_varios_seleccionada)
            btn.pack(side=tk.LEFT, padx=2, pady=1)

#####
    def mostrar_opciones_varios_seleccionada(self, opcion, boton):
        # Cambiar el color del botón seleccionado en el menú de cuentas
        if self.boton_seleccionado_cuentas:
            # Solo cambiar el color si el botón seleccionado aún existe
            try:
                self.boton_seleccionado_cuentas.config(bg='#d0cdc4')
            except tk.TclError:
                pass  # El botón ya no existe

        boton.config(bg='#b9b1ad')
        self.boton_seleccionado_cuentas = boton

        # Limpiar la configuración antes de mostrar nuevas opciones
        self.limpiar_configuracion()

        if opcion == "Archivos":
            self.mostrar_archivos()
        elif opcion == "Configuración":
            self.mostrar_configuracion()
        elif opcion == "Folio Solicitud CEP":
            self.mostrar_folio_solicitud_CEP()
######
    def mostrar_archivos(self):
        print("Mostrando el saldo actual...")

    def mostrar_configuracion(self):
        # Opciones del menú "Manto. Cuentas"
        opciones_manto_cuentas = ["Procesos Automáticos",
                                  "Mensajes H2H", "Generales", "CEP"]
        for opcion in opciones_manto_cuentas:
            btn = self.crear_boton(
                self.frames["configuracion"], opcion, self.mostrar_opciones_configuracion)
            btn.pack(side=tk.LEFT, padx=2, pady=1)

    def mostrar_opciones_configuracion(self, opcion, boton):
        # Cambiar el color del botón seleccionado en el menú de Manto. Cuentas
        if self.boton_seleccionado_configuracion:
            # Solo cambiar el color si el botón seleccionado aún existe
            try:
                self.boton_seleccionado_configuracion.config(bg='#d0cdc4')
            except tk.TclError:
                pass  # El botón ya no existe

        boton.config(bg='#b9b1ad')
        self.boton_seleccionado_configuracion = boton

        # Mostrar el mensaje y limpiar el menú
        self.mostrar_mensaje(opcion)

    def mostrar_folio_solicitud_CEP(self):
        print("Mostrando el saldo actual...")
######
    def mostrar_mensaje(self, opcion):
        print(f"{opcion} seleccionada")


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
