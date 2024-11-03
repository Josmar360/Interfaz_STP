import tkinter as tk
from Nueva_Empresa import Nueva_Empresa  # Importa el archivo Nueva_Empresa.py
#from Pantallas.Lista_Empresas import Lista_Empresas # Importa el archivo Lista_Empresas.py
import subprocess

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
                   b=btn: comando(t, b))
        return btn

    def mostrar_opciones_menu_principal(self, opcion, boton):
        if self.boton_seleccionado_principal:
            self.boton_seleccionado_principal.config(bg='#d0cdc4')

        boton.config(bg='#b9b1ad')
        self.boton_seleccionado_principal = boton

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
        for widget in self.frames["submenu"].winfo_children():
            widget.destroy()

    def limpiar_menu(self):
        for widget in self.frames["menu"].winfo_children():
            widget.destroy()
        self.boton_seleccionado_cuentas = None

    def limpiar_configuracion(self):
        for widget in self.frames["configuracion"].winfo_children():
            widget.destroy()
        self.boton_seleccionado_configuracion = None

    def mostrar_opciones_spei(self):
        opciones_spei = ["Recepción de Órdenes", "Cuentas",
                         "Catálogos", "Varios/Administración"]
        for opcion in opciones_spei:
            btn = self.crear_boton(
                self.frames["submenu"], opcion, self.mostrar_opciones_spei_seleccionada)
            btn.pack(side=tk.LEFT, padx=2, pady=1)

    def mostrar_opciones_spei_seleccionada(self, opcion, boton):
        if self.boton_seleccionado_spei:
            try:
                self.boton_seleccionado_spei.config(bg='#d0cdc4')
            except tk.TclError:
                pass

        boton.config(bg='#b9b1ad')
        self.boton_seleccionado_spei = boton

        self.limpiar_menu()
        self.limpiar_configuracion()

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
        opciones_cuentas = ["Saldo", "Manto. Cuentas",
                            "Manto. Empresas", "Configuración Empresas"]
        for opcion in opciones_cuentas:
            btn = self.crear_boton(
                self.frames["menu"], opcion, self.mostrar_opciones_cuentas_seleccionada)
            btn.pack(side=tk.LEFT, padx=2, pady=1)

    def mostrar_opciones_cuentas_seleccionada(self, opcion, boton):
        if self.boton_seleccionado_cuentas:
            try:
                self.boton_seleccionado_cuentas.config(bg='#d0cdc4')
            except tk.TclError:
                pass

        boton.config(bg='#b9b1ad')
        self.boton_seleccionado_cuentas = boton

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
        opciones_manto_cuentas = ["Propias",
                                  "Terceros", "Manto. Cuenta Terceros"]
        for opcion in opciones_manto_cuentas:
            btn = self.crear_boton(
                self.frames["configuracion"], opcion, self.mostrar_opciones_manto_cuentas_seleccionada)
            btn.pack(side=tk.LEFT, padx=2, pady=1)

    def mostrar_opciones_manto_cuentas_seleccionada(self, opcion, boton):
        if self.boton_seleccionado_configuracion:
            try:
                self.boton_seleccionado_configuracion.config(bg='#d0cdc4')
            except tk.TclError:
                pass

        boton.config(bg='#b9b1ad')
        self.boton_seleccionado_configuracion = boton

        self.mostrar_mensaje(opcion)

    def mostrar_manto_empresas(self):
        print("Mostrando mantenimiento de empresas...")

        # Botón 'Nueva' para llamar a la función de Nueva_Empresa.py
        btn_nueva = tk.Button(
            self.frames["configuracion"],
            text="Nueva",
            bg='#d0cdc4',
            fg='#8f7768',
            width=25,
            command=self.ejecutar_nueva_empresa
        )
        btn_nueva.pack(pady=5)

    def ejecutar_nueva_empresa(self):
        """Llama a la función 'Nueva_Empresa' del archivo Nueva_Empresa.py."""
        subprocess.run(["python", "Nueva_Empresa.py"])

    def mostrar_opciones_configuracion_empresas(self):
        opciones_configuracion = ["Generales", "Traspasos", "Tarjeta Débito"]
        for opcion in opciones_configuracion:
            btn = self.crear_boton(
                self.frames["configuracion"], opcion, self.mostrar_opciones_configuracion_empresas_seleccionada)
            btn.pack(side=tk.LEFT, padx=2, pady=1)

    def mostrar_opciones_configuracion_empresas_seleccionada(self, opcion, boton):
        if self.boton_seleccionado_configuracion:
            try:
                self.boton_seleccionado_configuracion.config(bg='#d0cdc4')
            except tk.TclError:
                pass

        boton.config(bg='#b9b1ad')
        self.boton_seleccionado_configuracion = boton

        # Limpia otras configuraciones previas si es necesario
        self.limpiar_configuracion()

        if opcion == "Generales":
            self.mostrar_generales()
        elif opcion == "Traspasos":
            self.mostrar_traspasos()
        elif opcion == "Tarjeta Débito":
            self.mostrar_tarjeta_debito()

    # Funciones separadas para cada opción de 'Configuración Empresas'
    def mostrar_generales(self):
        print("Mostrando la configuración de Generales...")

        # Botón 'Buscar' para llamar a la función de Lista_Empresas.py
        btn_nueva = tk.Button(
            self.frames["configuracion"],
            text="Buscar Empresa",
            bg='#d0cdc4',
            fg='#8f7768',
            width=25,
            command=self.ejecutar_nueva_interfaz
        )
        btn_nueva.pack(pady=5)

    def ejecutar_nueva_interfaz(self):
        """Llama a la función 'Listas Empresas' del archivo Listas_Empresas.py."""
        #Lista_Empresas()
        subprocess.run(["python", "Lista_Empresas.py"])

    def mostrar_traspasos(self):
        print("Mostrando la configuración de Traspasos...")
        # Aquí se puede agregar más widgets o botones específicos para 'Traspasos'

    def mostrar_tarjeta_debito(self):
        print("Mostrando la configuración de Tarjeta Débito...")
        # Aquí se puede agregar más widgets o botones específicos para 'Tarjeta Débito'

    def mostrar_catalogos(self):
        print("Mostrando los catálogos...")

    def mostrar_varios_administracion(self):
        opciones_varios = ["Archivos", "Configuración", "Folio Solicitud CEP"]
        for opcion in opciones_varios:
            btn = self.crear_boton(
                self.frames["menu"], opcion, self.mostrar_opciones_varios_seleccionada)
            btn.pack(side=tk.LEFT, padx=2, pady=1)

    def mostrar_opciones_varios_seleccionada(self, opcion, boton):
        if self.boton_seleccionado_cuentas:
            try:
                self.boton_seleccionado_cuentas.config(bg='#d0cdc4')
            except tk.TclError:
                pass

        boton.config(bg='#b9b1ad')
        self.boton_seleccionado_cuentas = boton

        self.limpiar_configuracion()

        if opcion == "Archivos":
            self.mostrar_archivos()
        elif opcion == "Configuración":
            self.mostrar_configuracion()
        elif opcion == "Folio Solicitud CEP":
            self.mostrar_folio_solicitud_CEP()

    def mostrar_archivos(self):
        print("Mostrando archivos...")

    def mostrar_configuracion(self):
        opciones_configuracion = [
            "Procesos Automáticos", "Mensajes H2H", "Generales", "CEP"]
        for opcion in opciones_configuracion:
            btn = self.crear_boton(
                self.frames["configuracion"], opcion, self.mostrar_opciones_configuracion)
            btn.pack(side=tk.LEFT, padx=2, pady=1)

    def mostrar_opciones_configuracion(self, opcion, boton):
        self.mostrar_mensaje(opcion)

    def mostrar_folio_solicitud_CEP(self):
        print("Mostrando folio de solicitud CEP...")

    def mostrar_mensaje(self, mensaje):
        print(f"Mostrando {mensaje}...")


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
