import sys
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector  # Asegúrate de tener este paquete instalado
from Crear_Nueva_Cuenta import Crear_Nueva_Cuenta


def Configuracion_Generales_Empresa(empresa_clave):
    root = tk.Tk()
    root.title("Generales")
    root.configure(bg="#d9f0ff")  # Fondo azul pastel claro para la ventana

    # Main Frame con diseño y color de fondo azul pastel
    main_frame = ttk.Frame(root, padding="15 15 15 15", style="Main.TFrame")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    main_frame.columnconfigure(0, weight=1)

    # Estilos de colores
    style = ttk.Style()
    style.configure("TLabel", background="#d9f0ff", font=("Arial", 10))
    style.configure("TCheckbutton", background="#d9f0ff")
    style.configure("TRadiobutton", background="#d9f0ff")
    style.configure("Main.TFrame", background="#d9f0ff")
    style.configure("Title.TLabel", font=(
        "Arial", 12, "bold"), background="#91ccea")
    style.configure("SubTitle.TLabel", font=(
        "Arial", 10, "bold"), background="#bde0fe")
    style.configure("TFrame", background="#bde0fe",
                    padding="10 10 10 10", relief="groove", borderwidth=2)

    # Sección: Título principal y subtítulo
    title_frame = ttk.Frame(main_frame, style="TFrame")
    title_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(title_frame, text=empresa_clave, style="SubTitle.TLabel").grid(
        row=0, column=0, sticky=tk.W)
    ttk.Label(title_frame, text="Generales", style="Title.TLabel").grid(
        row=1, column=0, sticky=tk.W)

    # Variables para los campos de la base de datos
    enviar_ordenes_var = tk.BooleanVar(value=False)
    selected_option = tk.StringVar(value="Participante indirecto del SPEI")
    valida_cuenta_var = tk.BooleanVar(value=False)
    omitir_validacion_var = tk.BooleanVar(value=False)
    usar_prefijo_sub_empresa_var = tk.BooleanVar(value=False)
    usar_prefijo_var = tk.BooleanVar(value=False)

    # Sección: Enviar órdenes
    orders_frame = ttk.Frame(main_frame, style="TFrame")
    orders_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Checkbutton(orders_frame, text="Enviar órdenes en horarios/días extendidos",
                    variable=enviar_ordenes_var).grid(row=0, column=0, sticky=tk.W)

    # Sección: Activar/Desactivar
    activate_frame = ttk.Frame(main_frame, style="TFrame")
    activate_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(activate_frame, text="Activar/Desactivar",
              style="SubTitle.TLabel").grid(row=0, column=0, sticky=tk.W)
    options = ["Participante indirecto del SPEI", "Empresa Crypto",
               "Persona Física con PD", "Participante Directo"]
    for i, option in enumerate(options, start=1):
        ttk.Radiobutton(activate_frame, text=option, variable=selected_option,
                        value=option).grid(row=i, column=0, sticky=tk.W)

    # Sección: Opciones adicionales
    additional_frame = ttk.Frame(main_frame, style="TFrame")
    additional_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Checkbutton(additional_frame, text="Validar cuenta destino",
                    variable=valida_cuenta_var).grid(row=0, column=0, sticky=tk.W)
    ttk.Checkbutton(additional_frame, text="Omitir validación del monto disponible antes de enviar operaciones",
                    variable=omitir_validacion_var).grid(row=1, column=0, sticky=tk.W)

    # Sección: Prefijo de Cuentas Propias
    prefix_frame = ttk.Frame(main_frame, style="TFrame")
    prefix_frame.grid(row=4, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(prefix_frame, text="Prefijo de Cuentas Propias",
              style="SubTitle.TLabel").grid(row=0, column=0, sticky=tk.W)
    ttk.Checkbutton(prefix_frame, text="Usar prefijo de Sub Empresa para recepción de órdenes",
                    variable=usar_prefijo_sub_empresa_var).grid(row=1, column=0, sticky=tk.W)
    ttk.Checkbutton(prefix_frame, text="Usar prefijo para recepción de órdenes",
                    variable=usar_prefijo_var).grid(row=2, column=0, sticky=tk.W)
    ttk.Label(prefix_frame, text="Prefijo:").grid(row=3, column=0, sticky=tk.W)
    prefijo_entry = ttk.Entry(prefix_frame, width=10)
    prefijo_entry.grid(row=3, column=1, sticky=tk.W, padx=(0, 10))
    prefijo_entry.insert(0, "")

    # Sección: Configuración del Subprefijo
    subprefix_frame = ttk.Frame(main_frame, style="TFrame")
    subprefix_frame.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(subprefix_frame, text="Configuración del Subprefijo",
              style="SubTitle.TLabel").grid(row=0, column=0, sticky=tk.W)
    ttk.Label(subprefix_frame, text="Longitud del Subprefijo:").grid(
        row=1, column=0, sticky=tk.W)
    subprefijo_entry = ttk.Entry(subprefix_frame, width=5)
    subprefijo_entry.grid(row=1, column=1, sticky=tk.W)
    subprefijo_entry.insert(0, "1")

    # Sección: Cuenta Concentradora
    concentrator_frame = ttk.Frame(main_frame, style="TFrame")
    concentrator_frame.grid(row=6, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(concentrator_frame, text="Cuenta Concentradora",
              style="SubTitle.TLabel").grid(row=0, column=0, sticky=tk.W)

    cuenta_combobox = ttk.Combobox(concentrator_frame, values=["Ninguno"])
    cuenta_combobox.grid(row=1, column=0, sticky=tk.W)
    cuenta_combobox.set("Ninguno")

    # Define la función Cuenta_Nueva
    def Cuenta_Nueva():
        # Obtén los valores que necesita (empresa_clave y prefijo)
        # Asegúrate de que estas variables están definidas en el contexto adecuado
        prefijo = prefijo_entry.get()  # Obtiene el prefijo desde la entrada

        # Llama a Crear_Nueva_Cuenta con los parámetros correctos
        Crear_Nueva_Cuenta(empresa_clave, prefijo)

    # Configura el botón para llamar a Cuenta_Nueva
    ttk.Button(concentrator_frame, text="Crear", command=Cuenta_Nueva).grid(
        row=1, column=1, sticky=tk.W)
    ttk.Label(concentrator_frame, text="Cuenta Concentradora para la empresa").grid(
        row=1, column=2, sticky=tk.W)

    # Sección: ACL
    acl_frame = ttk.Frame(main_frame, style="TFrame")
    acl_frame.grid(row=7, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(acl_frame, text="ACL", style="SubTitle.TLabel").grid(
        row=0, column=0, sticky=tk.W)
    acl_entry = ttk.Entry(acl_frame, width=30)
    acl_entry.grid(row=1, column=0, sticky=tk.W, padx=(0, 10))
    ttk.Label(acl_frame, text="IP/Subred válidos para servicios web (separados por espacios)").grid(
        row=1, column=1, sticky=tk.W)

    # Función para cargar la configuración existente

    def cargar_configuracion():
        try:
            conexion = mysql.connector.connect(
                user='root',
                password='Sarinha_3',
                host='localhost',
                database='STP'
            )
            cursor = conexion.cursor()

            # Cargar la configuración general
            cursor.execute(
                "SELECT * FROM configuracion_generales WHERE clave = %s", (empresa_clave,))
            result = cursor.fetchone()

            if result:
                (clave, enviar_ordenes, participacion_indirecto, empresa_crypto,
                persona_fisica_pd, participante_directo, valida_cuenta,
                omitir_validacion, usar_prefijo_sub_empresa, usar_prefijo,
                prefijo, longitud_subprefijo, cuenta_concentradora, acl) = result

                enviar_ordenes_var.set(enviar_ordenes)
                selected_option.set(participacion_indirecto)
                valida_cuenta_var.set(valida_cuenta)
                omitir_validacion_var.set(omitir_validacion)
                usar_prefijo_sub_empresa_var.set(usar_prefijo_sub_empresa)
                usar_prefijo_var.set(usar_prefijo)
                prefijo_entry.delete(0, tk.END)
                prefijo_entry.insert(0, prefijo)
                subprefijo_entry.delete(0, tk.END)
                subprefijo_entry.insert(0, longitud_subprefijo)
                acl_entry.delete(0, tk.END)
                acl_entry.insert(0, acl)

                # Consultar la concatenación de la cuenta concentradora
                cursor.execute("""
                    SELECT CONCAT(numero_banco, plaza, prefijo, numero, dv)
                    FROM cuenta
                    WHERE clave = %s
                """, (empresa_clave,))
                cuenta_result = cursor.fetchone()

                if cuenta_result and cuenta_result[0]:
                    cuenta_combobox.set(cuenta_result[0])
                else:
                    cuenta_combobox.set("Ninguno")

            cursor.close()
            conexion.close()
        except mysql.connector.Error as e:
            messagebox.showerror(
                "Error", f"Error al cargar la configuración: {e}")


    # Función para guardar la configuración
    def guardar_configuracion():
        try:
            conexion = mysql.connector.connect(
                user='root',
                password='Sarinha_3',
                host='localhost',
                database='STP'
            )
            cursor = conexion.cursor()

            # Comprobar si ya existe un registro para la clave
            cursor.execute(
                "SELECT * FROM configuracion_generales WHERE clave = %s", (empresa_clave,))
            result = cursor.fetchone()

            if result:
                # Actualizar el registro existente
                cursor.execute("""
                    UPDATE configuracion_generales SET 
                    enviar_ordenes_horario_dias_extendidos = %s,
                    participacion_indirecto_spei = %s,
                    empresa_crypto = %s,
                    persona_fisica_pd = %s,
                    participante_directo = %s,
                    valida_cuenta_destino = %s,
                    omitir_validacion_monto_disponible = %s,
                    usar_prefijo_sub_empresa = %s,
                    usar_prefijo_recepcion_ordenes = %s,
                    prefijo = %s,
                    longitud_subprefijo = %s,
                    cuenta_concentradora = %s,
                    acl = %s
                    WHERE clave = %s
                """, (
                    enviar_ordenes_var.get(),
                    selected_option.get() == "Participante indirecto del SPEI",
                    selected_option.get() == "Empresa Crypto",
                    selected_option.get() == "Persona Física con PD",
                    selected_option.get() == "Participante Directo",
                    valida_cuenta_var.get(),
                    omitir_validacion_var.get(),
                    usar_prefijo_sub_empresa_var.get(),
                    usar_prefijo_var.get(),
                    prefijo_entry.get(),
                    int(subprefijo_entry.get()),
                    cuenta_combobox.get(),
                    acl_entry.get(),
                    empresa_clave
                ))
            else:
                # Insertar nuevo registro
                cursor.execute("""
                    INSERT INTO configuracion_generales (
                        clave,
                        enviar_ordenes_horario_dias_extendidos,
                        participacion_indirecto_spei,
                        empresa_crypto,
                        persona_fisica_pd,
                        participante_directo,
                        valida_cuenta_destino,
                        omitir_validacion_monto_disponible,
                        usar_prefijo_sub_empresa,
                        usar_prefijo_recepcion_ordenes,
                        prefijo,
                        longitud_subprefijo,
                        cuenta_concentradora,
                        acl
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    empresa_clave,
                    enviar_ordenes_var.get(),
                    selected_option.get() == "Participante indirecto del SPEI",
                    selected_option.get() == "Empresa Crypto",
                    selected_option.get() == "Persona Física con PD",
                    selected_option.get() == "Participante Directo",
                    valida_cuenta_var.get(),
                    omitir_validacion_var.get(),
                    usar_prefijo_sub_empresa_var.get(),
                    usar_prefijo_var.get(),
                    prefijo_entry.get(),
                    int(subprefijo_entry.get()),
                    cuenta_combobox.get(),
                    acl_entry.get()
                ))

            conexion.commit()
            cursor.close()
            conexion.close()
            messagebox.showinfo(
                "Éxito", "Configuración guardada correctamente")
        except mysql.connector.Error as e:
            messagebox.showerror(
                "Error", f"Error al guardar la configuración: {e}")

    def actualizar_configuracion():
        cargar_configuracion()  # Llama a la función existente para recargar los datos desde la base de datos
        messagebox.showinfo("Actualización", "Datos actualizados correctamente")

    # Botones para guardar y salir
    buttons_frame = ttk.Frame(main_frame, style="TFrame")
    buttons_frame.grid(row=8, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Button(buttons_frame, text="Guardar", command=guardar_configuracion).grid(
        row=0, column=0, sticky=tk.W)
    ttk.Button(buttons_frame, text="Actualizar", command=actualizar_configuracion).grid(
        row=0, column=1, sticky=tk.W)
    ttk.Button(buttons_frame, text="Salir", command=root.destroy).grid(
        row=0, column=2, sticky=tk.W)

    # Cargar la configuración existente al abrir la ventana
    cargar_configuracion()

    root.mainloop()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        clave = sys.argv[1]  # Obtiene el argumento pasado
        Configuracion_Generales_Empresa(clave)
    else:
        print("No se proporcionó ninguna clave.")
