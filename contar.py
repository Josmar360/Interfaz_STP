import tkinter as tk
from tkinter import ttk
import mysql.connector
import sys


def Crear_Nueva_Cuenta(clave):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sarinha_3",
        database="STP"
    )
    cursor = conn.cursor()

    # Consulta para obtener los datos existentes de la cuenta
    select_query = "SELECT nombre_cuenta, numero_banco, plaza, prefijo, numero, dv, estado, notificacion_recibo_abonos FROM cuenta_cobranza WHERE clave = %s"
    cursor.execute(select_query, (clave,))
    result = cursor.fetchone()

    account_window = tk.Toplevel()
    account_window.title("Cuenta Cobranza")
    account_window.configure(bg="#d9f0ff")

    # Configura el tamaño y la posición de la ventana
    account_window.geometry("290x320+150+10")

    main_frame = ttk.Frame(
        account_window, padding="15 15 15 15", style="Main.TFrame")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    main_frame.columnconfigure(0, weight=1)

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

    name_frame = ttk.Frame(main_frame, style="TFrame")
    name_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(name_frame, text="Nombre de la Cuenta",
              style="SubTitle.TLabel").grid(row=0, column=0, sticky=tk.W)
    account_name_entry = ttk.Entry(name_frame, width=30)
    account_name_entry.grid(row=1, column=0, sticky=tk.W, padx=(0, 10))
    if result:
        account_name_entry.insert(0, result[0])

    account_number_frame = ttk.Frame(main_frame, style="TFrame")
    account_number_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(account_number_frame, text="Número de Cuenta",
              style="SubTitle.TLabel").grid(row=0, column=0, sticky=tk.W)
    ttk.Label(account_number_frame, text="Banco (3)").grid(
        row=1, column=0, sticky=tk.W)
    banco_entry = ttk.Entry(account_number_frame, width=5)
    banco_entry.grid(row=1, column=1, sticky=tk.W, padx=(0, 10))
    if result:
        banco_entry.insert(0, result[1])

    ttk.Label(account_number_frame, text="Plaza (3)").grid(
        row=2, column=0, sticky=tk.W)
    plaza_entry = ttk.Entry(account_number_frame, width=5)
    plaza_entry.grid(row=2, column=1, sticky=tk.W, padx=(0, 10))
    if result:
        plaza_entry.insert(0, result[2])

    ttk.Label(account_number_frame, text="Prefijo (0)").grid(
        row=3, column=0, sticky=tk.W)
    prefijo_entry = ttk.Entry(account_number_frame, width=5)
    prefijo_entry.grid(row=3, column=1, sticky=tk.W, padx=(0, 10))
    prefijo_entry.insert(0, "")  # Mostrar prefijo vacío
    if result and result[3]:
        prefijo_entry.insert(0, result[3])

    ttk.Label(account_number_frame, text="Número (11)").grid(
        row=4, column=0, sticky=tk.W)
    numero_entry = ttk.Entry(account_number_frame, width=10)
    numero_entry.grid(row=4, column=1, sticky=tk.W, padx=(0, 10))
    if result:
        numero_entry.insert(0, result[4])

    ttk.Label(account_number_frame, text="DV (1)").grid(
        row=5, column=0, sticky=tk.W)
    dv_entry = ttk.Entry(account_number_frame, width=5)
    dv_entry.grid(row=5, column=1, sticky=tk.W, padx=(0, 10))
    if result:
        dv_entry.insert(0, result[5])

    ttk.Label(account_number_frame, text="Estado").grid(
        row=6, column=0, sticky=tk.W)
    state_combobox = ttk.Combobox(
        account_number_frame, values=["Activa", "Inactiva"])
    state_combobox.grid(row=6, column=1, sticky=tk.W)
    state_combobox.set("Activa" if not result else result[6])

    notification_frame = ttk.Frame(main_frame, style="TFrame")
    notification_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=5)
    notification_var = tk.BooleanVar(value=False if not result else result[7])
    ttk.Checkbutton(notification_frame, text="Activar Notificación de Recepción de Abonos",
                    variable=notification_var).grid(row=0, column=0, sticky=tk.W)

    ttk.Button(main_frame, text="Aplicar", command=lambda: save_account(
        clave, account_name_entry.get(), banco_entry.get(), plaza_entry.get(), "", numero_entry.get(), dv_entry.get(), state_combobox.get(), notification_var.get())).grid(row=3, column=0, sticky=tk.E, pady=20)

    cursor.close()
    conn.close()


def save_account(clave, nombre_cuenta, numero_banco, plaza, prefijo, numero, dv, estado, notificacion):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sarinha_3",
        database="STP"
    )
    cursor = conn.cursor()

    # Verificar si la cuenta ya existe
    select_query = "SELECT * FROM cuenta_cobranza WHERE clave = %s"
    cursor.execute(select_query, (clave,))
    existing_account = cursor.fetchone()

    if existing_account:
        update_query = """UPDATE cuenta_cobranza
                          SET nombre_cuenta = %s, numero_banco = %s, plaza = %s, prefijo = %s, numero = %s, dv = %s, estado = %s, notificacion_recibo_abonos = %s
                          WHERE clave = %s"""
        cursor.execute(update_query, (nombre_cuenta, numero_banco,
                       plaza, prefijo, numero, dv, estado, notificacion, clave))
        print(f"Cuenta '{nombre_cuenta}' actualizada.")
    else:
        insert_query = """INSERT INTO cuenta_cobranza (clave, nombre_cuenta, numero_banco, plaza, prefijo, numero, dv, estado, notificacion_recibo_abonos)
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(insert_query, (clave, nombre_cuenta, numero_banco,
                       plaza, prefijo, numero, dv, estado, notificacion))
        print(f"Cuenta '{nombre_cuenta}' guardada.")

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        root = tk.Tk()
        root.withdraw()
        clave = sys.argv[1]  # Obtiene el argumento pasado
        Crear_Nueva_Cuenta(clave)
        root.mainloop()
    else:
        print("No se proporcionó ninguna clave.")

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import sys

def create_config_window(clave):
    root = tk.Tk()
    root.title("Configuración Varios")
    root.geometry("500x670+150+10")
    root.configure(bg="#d9f0ff")  # Fondo azul pastel claro para la ventana

    # Estilos de colores
    header_color = "#91ccea"
    section_color = "#bde0fe"

    # Crear encabezado
    header_frame = tk.Frame(root, bg="#d9f0ff")
    header_frame.pack(fill=tk.X, pady=(5, 10))

    header_label = tk.Label(header_frame, text=clave,
                            bg=header_color, fg="white", font=("Arial", 16, "bold"))
    header_label.pack(side=tk.TOP, fill=tk.X)

    # Crear sección "Generales"
    section1 = tk.LabelFrame(root, text="Generales", bg=section_color, font=(
        "Arial", 12, "bold"), padx=10, pady=5)
    section1.pack(fill=tk.X, padx=10, pady=5)

    # Elementos de "Generales"
    generales_checks = [
        "Editar Órdenes en Módulo de Autorización",
        "Autorizar Órdenes propias"
    ]
    generales_vars = []
    for text in generales_checks:
        var = tk.BooleanVar(value=False)
        tk.Checkbutton(section1, text=text, variable=var, bg=section_color, font=(
            "Arial", 10)).grid(sticky="w", pady=2, padx=5)
        generales_vars.append(var)

    # Subtítulos de columnas
    tk.Label(section1, text="Medio de Entrega", bg=section_color, font=(
        "Arial", 10, "bold")).grid(row=len(generales_checks), column=0, pady=2, padx=5, sticky="w")
    tk.Label(section1, text="Usuario por Default", bg=section_color, font=(
        "Arial", 10, "bold")).grid(row=len(generales_checks), column=1, pady=2, padx=5, sticky="w")

    # Filas para medios de entrega con Combobox
    medios = ["H2H", "DevolucionesH2H", "Auto Cobro"]
    user_comboboxes = []

    # Crear los Comboboxes para cada medio de entrega
    for i, medio in enumerate(medios):
        tk.Label(section1, text=medio, bg=section_color, font=(
            "Arial", 10)).grid(sticky="w", pady=2, padx=5)
        user_combobox = ttk.Combobox(
            section1, values=["Ninguno", "engen ui"], state="readonly", font=("Arial", 9))
        user_combobox.set("Ninguno")
        user_combobox.grid(row=len(generales_checks) +
                           1 + i, column=1, padx=5, pady=2)
        user_comboboxes.append(user_combobox)

    # Crear sección "Validación de Cuentas"
    section2 = tk.LabelFrame(root, text="Validación de Cuentas", bg=section_color, font=(
        "Arial", 12, "bold"), padx=10, pady=5)
    section2.pack(fill=tk.X, padx=10, pady=5)

    # Cabeceras de la tabla de Validación de Cuentas
    headers = ["Medio de Entrega", "Clabe", "Débito", "Celular"]
    for col, header in enumerate(headers):
        tk.Label(section2, text=header, bg=section_color, font=(
            "Arial", 9, "bold")).grid(row=0, column=col, padx=5, pady=2)

    # Filas con checkbox para cada medio de entrega
    medios_validacion = ["EnlaceFinanciero", "Archivo",
                         "H2H", "DevolucionesH2H", "Auto Cobro"]

    # Variables para los checkboxes
    checkbox_values = {}

    for i, medio in enumerate(medios_validacion, start=1):
        tk.Label(section2, text=medio, bg=section_color, font=("Arial", 9)).grid(
            row=i, column=0, sticky="w", padx=5, pady=2)

        var_clabe = tk.BooleanVar(value=False)  # Checkbox Clabe
        var_debito = tk.BooleanVar(value=False)  # Checkbox Débito
        var_celular = tk.BooleanVar(value=False)  # Checkbox Celular

        checkbox_values[medio] = {
            "Clabe": var_clabe,
            "Débito": var_debito,
            "Celular": var_celular
        }

        tk.Checkbutton(section2, variable=var_clabe, bg=section_color).grid(
            row=i, column=1, padx=5, pady=2)
        tk.Checkbutton(section2, variable=var_debito, bg=section_color).grid(
            row=i, column=2, padx=5, pady=2)
        tk.Checkbutton(section2, variable=var_celular, bg=section_color).grid(
            row=i, column=3, padx=5, pady=2)

    # Crear sección "Supervisores"
    section3 = tk.LabelFrame(root, text="Supervisores", bg=section_color, font=(
        "Arial", 12, "bold"), padx=10, pady=5)
    section3.pack(fill=tk.X, padx=10, pady=5)

    supervisores_checks = [
        "Liberar órdenes de supervisados",
        "Modificar órdenes de supervisados"
    ]
    supervisores_vars = []
    for text in supervisores_checks:
        var = tk.BooleanVar(value=False)
        tk.Checkbutton(section3, text=text, variable=var, bg=section_color, font=(
            "Arial", 10)).grid(sticky="w", pady=2, padx=5)
        supervisores_vars.append(var)

    # Crear sección "IVA (%)"
    section4 = tk.Frame(root, bg=section_color)
    section4.pack(fill=tk.X, padx=10, pady=5)

    tk.Label(section4, text="IVA (%)", bg=section_color, font=(
        "Arial", 10)).grid(row=0, column=0, sticky="w", pady=5, padx=5)
    iva_entry = tk.Entry(section4, font=("Arial", 10))
    iva_entry.grid(row=0, column=1, padx=5)

    # Función para insertar los resultados en la base de datos
    def save_to_database():
        try:
            # Conectar a la base de datos
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Sarinha_3',
                database='STP'
            )

            cursor = connection.cursor()

            # Preparar la consulta de inserción
            query = """
            INSERT INTO configuracion (
                clave, 
                Generales_Autorizacion_Activar,
                Generales_Propias_Activar,
                Generales_H2H_Default,
                Generales_DevolucionesH2H_Default,
                Generales_AutoCobro_Default,
                ValidacionCuentas_EnlaceFinanciero_Clave,
                ValidacionCuentas_EnlaceFinanciero_Debito,
                ValidacionCuentas_EnlaceFinanciero_Celular,
                ValidacionCuentas_Archivo_Clave,
                ValidacionCuentas_Archivo_Debito,
                ValidacionCuentas_Archivo_Celular,
                ValidacionCuentas_H2H_Clave,
                ValidacionCuentas_H2H_Debito,
                ValidacionCuentas_H2H_Celular,
                ValidacionCuentas_DevolucionesH2H_Clave,
                ValidacionCuentas_DevolucionesH2H_Debito,
                ValidacionCuentas_DevolucionesH2H_Celular,
                ValidacionCuentas_AutoCobro_Clave,
                ValidacionCuentas_AutoCobro_Debito,
                ValidacionCuentas_AutoCobro_Celular,
                Supervisores_Liberar_Activar,
                Supervisores_Modificar_Activar,
                IVA_Porcentaje
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            # Preparar los valores
            values = (
                clave,  # clave
                generales_vars[0].get(),  # Generales_Autorizacion_Activar
                generales_vars[1].get(),  # Generales_Propias_Activar
                user_comboboxes[0].get(),  # Generales_H2H_Default
                user_comboboxes[1].get(),  # Generales_DevolucionesH2H_Default
                user_comboboxes[2].get(),  # Generales_AutoCobro_Default
                # ValidacionCuentas_EnlaceFinanciero_Clave
                checkbox_values["EnlaceFinanciero"]["Clabe"].get(),
                # ValidacionCuentas_EnlaceFinanciero_Debito
                checkbox_values["EnlaceFinanciero"]["Débito"].get(),
                # ValidacionCuentas_EnlaceFinanciero_Celular
                checkbox_values["EnlaceFinanciero"]["Celular"].get(),
                # ValidacionCuentas_Archivo_Clave
                checkbox_values["Archivo"]["Clabe"].get(),
                # ValidacionCuentas_Archivo_Debito
                checkbox_values["Archivo"]["Débito"].get(),
                # ValidacionCuentas_Archivo_Celular
                checkbox_values["Archivo"]["Celular"].get(),
                # ValidacionCuentas_H2H_Clave
                checkbox_values["H2H"]["Clabe"].get(),
                # ValidacionCuentas_H2H_Debito
                checkbox_values["H2H"]["Débito"].get(),
                # ValidacionCuentas_H2H_Celular
                checkbox_values["H2H"]["Celular"].get(),
                # ValidacionCuentas_DevolucionesH2H_Clave
                checkbox_values["DevolucionesH2H"]["Clabe"].get(),
                # ValidacionCuentas_DevolucionesH2H_Debito
                checkbox_values["DevolucionesH2H"]["Débito"].get(),
                # ValidacionCuentas_DevolucionesH2H_Celular
                checkbox_values["DevolucionesH2H"]["Celular"].get(),
                # ValidacionCuentas_AutoCobro_Clave
                checkbox_values["Auto Cobro"]["Clabe"].get(),
                # ValidacionCuentas_AutoCobro_Debito
                checkbox_values["Auto Cobro"]["Débito"].get(),
                # ValidacionCuentas_AutoCobro_Celular
                checkbox_values["Auto Cobro"]["Celular"].get(),
                supervisores_vars[0].get(),  # Supervisores_Liberar_Activar
                supervisores_vars[1].get(),  # Supervisores_Modificar_Activar
                iva_entry.get()  # IVA_Porcentaje
            )

            # Ejecutar la consulta
            cursor.execute(query, values)
            connection.commit()

            # Mensaje de éxito
            messagebox.showinfo(
                "Éxito", "Configuración guardada correctamente.")
            #root.destroy()  # Cerrar la ventana después de guardar

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al guardar configuración: {
                                 err}")  # Manejo de errores
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    # Botón para guardar configuración
    save_button = tk.Button(root, text="Guardar", command=save_to_database,
                            bg="#4caf50", fg="white", font=("Arial", 12))
    save_button.pack(pady=(10, 5))

    root.mainloop()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        clave = sys.argv[1]  # Obtiene el argumento pasado
        create_config_window(clave)
    else:
        print("No se proporcionó ninguna clave.")

import tkinter as tk
import mysql.connector
from tkinter import ttk
import sys


def main(clave):
    root = tk.Tk() 
    root.title("Procesos Automáticos")
    root.geometry("560x730+150+10")
    root.configure(bg="#d9f0ff")

    header_color = "#91ccea"
    section_color = "#bde0fe"

    # Sección del encabezado
    header_frame = tk.Frame(root, bg="#d9f0ff")
    header_frame.pack(fill=tk.X, pady=(1, 1))

    header_label = tk.Label(header_frame, text=clave,
                            bg=header_color, fg="white", font=("Arial", 12))
    header_label.pack(side=tk.TOP, fill=tk.X)

    # Sección de Autorización de órdenes
    section1 = tk.LabelFrame(root, text="Autorización de órdenes",
                             bg=section_color, font=("Arial", 12), padx=10, pady=5)
    section1.pack(fill=tk.X, padx=10, pady=5)

    # Variables para almacenar los valores de los checkbuttons y entradas
    var_manual = tk.BooleanVar()
    var_archivo = tk.BooleanVar()
    var_h2h = tk.BooleanVar()
    var_devoluciones_h2h = tk.BooleanVar()
    var_auto_cobro = tk.BooleanVar()

    # Variables para almacenar los datos de entrada
    autorizacion_ordenes_manual_activar = tk.BooleanVar()
    autorizacion_ordenes_manual_default = tk.StringVar()
    autorizacion_ordenes_manual_monto_maximo = tk.DoubleVar()

    autorizacion_ordenes_archivo_activar = tk.BooleanVar()
    autorizacion_ordenes_archivo_default = tk.StringVar()
    autorizacion_ordenes_archivo_monto_maximo = tk.DoubleVar()

    autorizacion_ordenes_h2h_activar = tk.BooleanVar()
    autorizacion_ordenes_h2h_default = tk.StringVar()
    autorizacion_ordenes_h2h_monto_maximo = tk.DoubleVar()

    autorizacion_ordenes_devoluciones_h2h_activar = tk.BooleanVar()
    autorizacion_ordenes_devoluciones_h2h_default = tk.StringVar()
    autorizacion_ordenes_devoluciones_h2h_monto_maximo = tk.DoubleVar()

    autorizacion_ordenes_auto_cobro_activar = tk.BooleanVar()
    autorizacion_ordenes_auto_cobro_default = tk.StringVar()
    autorizacion_ordenes_auto_cobro_monto_maximo = tk.DoubleVar()

    # Funciones para crear encabezados y controles de la sección de Autorización de órdenes
    def create_section_headers(frame):
        tk.Label(frame, text="Activar/Desactivar",
                 bg=section_color).grid(row=0, column=0, pady=2, padx=5)
        tk.Label(frame, text="Medio de entrega", bg=section_color).grid(
            row=0, column=1, pady=2, padx=5)
        tk.Label(frame, text="Usuario por default", bg=section_color).grid(
            row=0, column=2, pady=2, padx=5)
        tk.Label(frame, text="Monto máximo", bg=section_color).grid(
            row=0, column=3, pady=2, padx=5)

    def create_checkbox_entry(frame, text, row, var_activar, var_default, var_monto):
        tk.Checkbutton(frame, variable=var_activar, bg=section_color).grid(
            row=row, column=0, sticky="w", pady=2, padx=(10, 5))
        tk.Label(frame, text=text, bg=section_color).grid(
            row=row, column=1, pady=2, padx=5)
        user_combobox = ttk.Combobox(
            frame, values=["Ninguno", "engen ui"], textvariable=var_default, state="readonly")
        user_combobox.set("Ninguno")
        user_combobox.grid(row=row, column=2, padx=5)
        tk.Entry(frame, textvariable=var_monto).grid(row=row, column=3, padx=5)

    # Crear controles para la sección de Autorización de órdenes
    create_section_headers(section1)
    create_checkbox_entry(section1, "Devolución Manual", 1, autorizacion_ordenes_manual_activar,
                          autorizacion_ordenes_manual_default, autorizacion_ordenes_manual_monto_maximo)
    create_checkbox_entry(section1, "Archivo", 2, autorizacion_ordenes_archivo_activar,
                          autorizacion_ordenes_archivo_default, autorizacion_ordenes_archivo_monto_maximo)
    create_checkbox_entry(section1, "H2H", 3, autorizacion_ordenes_h2h_activar,
                          autorizacion_ordenes_h2h_default, autorizacion_ordenes_h2h_monto_maximo)
    create_checkbox_entry(section1, "Devoluciones H2H", 4, autorizacion_ordenes_devoluciones_h2h_activar,
                          autorizacion_ordenes_devoluciones_h2h_default, autorizacion_ordenes_devoluciones_h2h_monto_maximo)
    create_checkbox_entry(section1, "Auto Cobro", 5, autorizacion_ordenes_auto_cobro_activar,
                          autorizacion_ordenes_auto_cobro_default, autorizacion_ordenes_auto_cobro_monto_maximo)

    # Sección de Autorización de traspasos
    section2 = tk.LabelFrame(root, text="Autorización de traspasos",
                             bg=section_color, font=("Arial", 12), padx=10, pady=1)
    section2.pack(fill=tk.X, padx=10, pady=5)

    # Variables para almacenar los datos de entrada de la sección de traspasos
    autorizacion_traspasos_h2h_activar = tk.BooleanVar()
    autorizacion_traspasos_h2h_default = tk.StringVar()

    autorizacion_traspasos_devoluciones_h2h_activar = tk.BooleanVar()
    autorizacion_traspasos_devoluciones_h2h_default = tk.StringVar()

    autorizacion_traspasos_auto_cobro_activar = tk.BooleanVar()
    autorizacion_traspasos_auto_cobro_default = tk.StringVar()

    # Funciones para crear encabezados y controles de la sección de Autorización de traspasos
    def create_section_headers_traspasos(frame):
        tk.Label(frame, text="Activar/Desactivar",
                 bg=section_color).grid(row=0, column=0, pady=2, padx=5)
        tk.Label(frame, text="Medio de entrega", bg=section_color).grid(
            row=0, column=1, pady=2, padx=5)
        tk.Label(frame, text="Usuario por default", bg=section_color).grid(
            row=0, column=2, pady=2, padx=5)

    def create_checkbox_entry_traspasos(frame, text, row, var_activar, var_default):
        tk.Checkbutton(frame, variable=var_activar, bg=section_color).grid(
            row=row, column=0, sticky="w", pady=2, padx=(10, 5))
        tk.Label(frame, text=text, bg=section_color).grid(
            row=row, column=1, pady=2, padx=5)
        user_combobox = ttk.Combobox(
            frame, values=["Ninguno", "engen ui"], textvariable=var_default, state="readonly")
        user_combobox.set("Ninguno")
        user_combobox.grid(row=row, column=2, padx=5)

    # Crear controles para la sección de Autorización de traspasos
    create_section_headers_traspasos(section2)
    create_checkbox_entry_traspasos(section2, "H2H", 1, autorizacion_traspasos_h2h_activar,
                                    autorizacion_traspasos_h2h_default)
    create_checkbox_entry_traspasos(section2, "Devoluciones H2H", 2, autorizacion_traspasos_devoluciones_h2h_activar,
                                    autorizacion_traspasos_devoluciones_h2h_default)
    create_checkbox_entry_traspasos(section2, "Auto Cobro", 3, autorizacion_traspasos_auto_cobro_activar,
                                    autorizacion_traspasos_auto_cobro_default)

    # Sección de Devoluciones Automáticas
    section3 = tk.LabelFrame(root, text="Devoluciones Automáticas",
                             bg=section_color, font=("Arial", 12), padx=10, pady=5)
    section3.pack(fill=tk.X, padx=10, pady=5)

    # Variables para almacenar los datos de entrada de la sección de Devoluciones Automáticas
    devoluciones_rastreo_duplicado_activar = tk.BooleanVar()
    devoluciones_rastreo_duplicado_causa = tk.StringVar()
    devoluciones_rastreo_duplicado_autorizar = tk.BooleanVar()

    devoluciones_error_detalle_activar = tk.BooleanVar()
    devoluciones_error_detalle_causa = tk.StringVar()
    devoluciones_error_detalle_autorizar = tk.BooleanVar()

    devoluciones_caracter_invalido_activar = tk.BooleanVar()
    devoluciones_caracter_invalido_causa = tk.StringVar()
    devoluciones_caracter_invalido_autorizar = tk.BooleanVar()

    devoluciones_cuenta_invalida_activar = tk.BooleanVar()
    devoluciones_cuenta_invalida_causa = tk.StringVar()
    devoluciones_cuenta_invalida_autorizar = tk.BooleanVar()

    devoluciones_tipo_cta_beneficiario_activar = tk.BooleanVar()
    devoluciones_tipo_cta_beneficiario_causa = tk.StringVar()
    devoluciones_tipo_cta_beneficiario_autorizar = tk.BooleanVar()

    devoluciones_tipo_cta_ordenante_activar = tk.BooleanVar()
    devoluciones_tipo_cta_ordenante_causa = tk.StringVar()
    devoluciones_tipo_cta_ordenante_autorizar = tk.BooleanVar()

    devoluciones_tipo_pago_activar = tk.BooleanVar()
    devoluciones_tipo_pago_causa = tk.StringVar()
    devoluciones_tipo_pago_autorizar = tk.BooleanVar()

    # Funciones para crear encabezados y controles de la sección de Devoluciones Automáticas
    def create_section_headers_devoluciones(frame):
        tk.Label(frame, text="Activar/Desactivar",
                 bg=section_color).grid(row=0, column=0, pady=2, padx=5)
        tk.Label(frame, text="Descripción",
                 bg=section_color).grid(row=0, column=1, pady=2, padx=5)
        tk.Label(frame, text="Causa de devolución", bg=section_color).grid(
            row=0, column=2, pady=2, padx=5)
        tk.Label(frame, text="Autorizar", bg=section_color).grid(
            row=0, column=3, pady=2, padx=5)

    def create_checkbox_entry_devoluciones(frame, text, reasons, row, var_activar, var_causa, var_autorizar):
        tk.Checkbutton(frame, variable=var_activar, bg=section_color).grid(
            row=row, column=0, sticky="w", pady=2, padx=(10, 5))
        tk.Label(frame, text=text, bg=section_color).grid(
            row=row, column=1, pady=2, padx=5)
        reason_combobox = ttk.Combobox(frame, values=reasons, state="readonly")
        reason_combobox.set(
            "Falta información mandatoria para completar el pago")
        reason_combobox.grid(row=row, column=2, padx=5)
        # tk.Entry(frame, textvariable=var_causa).grid(row=row, column=1, padx=5)
        tk.Checkbutton(frame, variable=var_autorizar, bg=section_color).grid(
            row=row, column=3, pady=2, padx=(10, 5))

    # Crear controles para la sección de Devoluciones Automáticas
    create_section_headers_devoluciones(section3)
    reasons = ["Falta información mandatoria para completar el pago",
               "Carácter inválido", "Cuenta inexistente", "Tipo de pago erróneo"]
    create_checkbox_entry_devoluciones(section3, "Por Rastreo Duplicado", reasons, 1,
                                       devoluciones_rastreo_duplicado_activar,
                                       devoluciones_rastreo_duplicado_causa,
                                       devoluciones_rastreo_duplicado_autorizar)
    create_checkbox_entry_devoluciones(section3, "Por error en detalle", reasons, 2,
                                       devoluciones_error_detalle_activar,
                                       devoluciones_error_detalle_causa,
                                       devoluciones_error_detalle_autorizar)
    create_checkbox_entry_devoluciones(section3, "Por carácter inválido", reasons, 3,
                                       devoluciones_caracter_invalido_activar,
                                       devoluciones_caracter_invalido_causa,
                                       devoluciones_caracter_invalido_autorizar)
    create_checkbox_entry_devoluciones(section3, "Por Cuenta Inválida", reasons, 4,
                                       devoluciones_cuenta_invalida_activar,
                                       devoluciones_cuenta_invalida_causa,
                                       devoluciones_cuenta_invalida_autorizar)
    create_checkbox_entry_devoluciones(section3, "Por Tipo de Cta. Beneficiario", reasons, 5,
                                       devoluciones_tipo_cta_beneficiario_activar,
                                       devoluciones_tipo_cta_beneficiario_causa,
                                       devoluciones_tipo_cta_beneficiario_autorizar)
    create_checkbox_entry_devoluciones(section3, "Por Tipo de Cta. Ordenante", reasons, 6,
                                       devoluciones_tipo_cta_ordenante_activar,
                                       devoluciones_tipo_cta_ordenante_causa,
                                       devoluciones_tipo_cta_ordenante_autorizar)
    create_checkbox_entry_devoluciones(section3, "Por Tipo de Pago", reasons, 7,
                                       devoluciones_tipo_pago_activar,
                                       devoluciones_tipo_pago_causa,
                                       devoluciones_tipo_pago_autorizar)

    def insertar_datos():
        # Conexión a la base de datos
        #clave = clave_entry.get().strip()
        #print(f"Valor de clave obtenido: {clave}") 
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sarinha_3",
            database="STP"
        )

        cursor = conexion.cursor()

        # Consulta SQL para insertar los datos
        consulta = """
        INSERT INTO procesos_automaticos (
            clave,
            autorizacion_ordenes_manual_activar,
            autorizacion_ordenes_manual_default,
            autorizacion_ordenes_manual_monto_maximo,
            autorizacion_ordenes_archivo_activar,
            autorizacion_ordenes_archivo_default,
            autorizacion_ordenes_archivo_monto_maximo,
            autorizacion_ordenes_h2h_activar,
            autorizacion_ordenes_h2h_default,
            autorizacion_ordenes_h2h_monto_maximo,
            autorizacion_ordenes_devoluciones_h2h_activar,
            autorizacion_ordenes_devoluciones_h2h_default,
            autorizacion_ordenes_devoluciones_h2h_monto_maximo,
            autorizacion_ordenes_auto_cobro_activar,
            autorizacion_ordenes_auto_cobro_default,
            autorizacion_ordenes_auto_cobro_monto_maximo,
            autorizacion_traspasos_h2h_activar,
            autorizacion_traspasos_h2h_default,
            autorizacion_traspasos_devoluciones_h2h_activar,
            autorizacion_traspasos_devoluciones_h2h_default,
            autorizacion_traspasos_auto_cobro_activar,
            autorizacion_traspasos_auto_cobro_default,
            devoluciones_rastreo_duplicado_activar,
            devoluciones_rastreo_duplicado_causa,
            devoluciones_rastreo_duplicado_autorizar,
            devoluciones_error_detalle_activar,
            devoluciones_error_detalle_causa,
            devoluciones_error_detalle_autorizar,
            devoluciones_caracter_invalido_activar,
            devoluciones_caracter_invalido_causa,
            devoluciones_caracter_invalido_autorizar,
            devoluciones_cuenta_invalida_activar,
            devoluciones_cuenta_invalida_causa,
            devoluciones_cuenta_invalida_autorizar,
            devoluciones_tipo_cta_beneficiario_activar,
            devoluciones_tipo_cta_beneficiario_causa,
            devoluciones_tipo_cta_beneficiario_autorizar,
            devoluciones_tipo_cta_ordenante_activar,
            devoluciones_tipo_cta_ordenante_causa,
            devoluciones_tipo_cta_ordenante_autorizar,
            devoluciones_tipo_pago_activar,
            devoluciones_tipo_pago_causa,
            devoluciones_tipo_pago_autorizar
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        valores = (
            clave,
            autorizacion_ordenes_manual_activar.get(),
            autorizacion_ordenes_manual_default.get(),
            autorizacion_ordenes_manual_monto_maximo.get(),
            autorizacion_ordenes_archivo_activar.get(),
            autorizacion_ordenes_archivo_default.get(),
            autorizacion_ordenes_archivo_monto_maximo.get(),
            autorizacion_ordenes_h2h_activar.get(),
            autorizacion_ordenes_h2h_default.get(),
            autorizacion_ordenes_h2h_monto_maximo.get(),
            autorizacion_ordenes_devoluciones_h2h_activar.get(),
            autorizacion_ordenes_devoluciones_h2h_default.get(),
            autorizacion_ordenes_devoluciones_h2h_monto_maximo.get(),
            autorizacion_ordenes_auto_cobro_activar.get(),
            autorizacion_ordenes_auto_cobro_default.get(),
            autorizacion_ordenes_auto_cobro_monto_maximo.get(),
            autorizacion_traspasos_h2h_activar.get(),
            autorizacion_traspasos_h2h_default.get(),
            autorizacion_traspasos_devoluciones_h2h_activar.get(),
            autorizacion_traspasos_devoluciones_h2h_default.get(),
            autorizacion_traspasos_auto_cobro_activar.get(),
            autorizacion_traspasos_auto_cobro_default.get(),
            devoluciones_rastreo_duplicado_activar.get(),
            devoluciones_rastreo_duplicado_causa.get(),
            devoluciones_rastreo_duplicado_autorizar.get(),
            devoluciones_error_detalle_activar.get(),
            devoluciones_error_detalle_causa.get(),
            devoluciones_error_detalle_autorizar.get(),
            devoluciones_caracter_invalido_activar.get(),
            devoluciones_caracter_invalido_causa.get(),
            devoluciones_caracter_invalido_autorizar.get(),
            devoluciones_cuenta_invalida_activar.get(),
            devoluciones_cuenta_invalida_causa.get(),
            devoluciones_cuenta_invalida_autorizar.get(),
            devoluciones_tipo_cta_beneficiario_activar.get(),
            devoluciones_tipo_cta_beneficiario_causa.get(),
            devoluciones_tipo_cta_beneficiario_autorizar.get(),
            devoluciones_tipo_cta_ordenante_activar.get(),
            devoluciones_tipo_cta_ordenante_causa.get(),
            devoluciones_tipo_cta_ordenante_autorizar.get(),
            devoluciones_tipo_pago_activar.get(),
            devoluciones_tipo_pago_causa.get(),
            devoluciones_tipo_pago_autorizar.get()
        )

        cursor.execute(consulta, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Datos insertados exitosamente en la base de datos.")

    # Botón de "Aplicar" en la parte inferior derecha

    apply_button = tk.Button(root, text="Aceptar", bg="#91ccea", fg="white", font=(
        "Arial", 12), activebackground="#bde0fe", activeforeground="black", command=insertar_datos)
    apply_button.pack(padx=10, pady=5)

    root.mainloop()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        clave = 'ENGEN'
        clave = sys.argv[1]  # Obtiene el argumento pasado
        main(clave)
    else:
        print("No se proporcionó ninguna clave.")

import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


def save_company():
    # Obtener los datos de la entrada
    clave = entry_clave.get()
    nombre = entry_nombre.get()
    razon_social = entry_razon_social.get()
    rfc = entry_rfc.get()
    direccion = entry_direccion.get()
    nombre_ordenante = entry_nombre_ordenante.get()
    rfc_ordenante = entry_rfc_ordenante.get()
    empresa_activa = var_empresa_activa.get()

    # Conectar a la base de datos MySQL
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sarinha_3",
            database="STP"
        )
        cursor = conn.cursor()

        # Insertar los datos en la tabla
        query = """
        INSERT INTO empresa (clave, nombre, razon_social, rfc, direccion, nombre_ordenante, rfc_ordenante, empresa_activa)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (clave, nombre, razon_social, rfc, direccion,
                  nombre_ordenante, rfc_ordenante, empresa_activa)

        cursor.execute(query, values)
        conn.commit()

        messagebox.showinfo("Éxito", "Empresa guardada correctamente.")
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al guardar la empresa: {err}")


def Nueva_Empresa():
    global entry_clave, entry_nombre, entry_razon_social, entry_rfc, entry_direccion, entry_nombre_ordenante, entry_rfc_ordenante, var_empresa_activa
    root = tk.Tk()
    root.geometry("350x270+150+10")
    root.title("Nueva Empresa")
    root.configure(bg="#d9f0ff")

    # Configuración de frames y entradas
    main_frame = ttk.Frame(root, padding="15 15 15 15", style="Main.TFrame")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    main_frame.columnconfigure(0, weight=1)

    # Estilos
    style = ttk.Style()
    style.configure("TLabel", background="#d9f0ff", font=("Arial", 10))
    style.configure("Main.TFrame", background="#d9f0ff")
    style.configure("SubTitle.TLabel", font=(
        "Arial", 10, "bold"), background="#bde0fe")
    style.configure("TFrame", background="#bde0fe",
                    padding="10 10 10 10", relief="groove", borderwidth=2)

    # Sección: Empresa
    company_frame = ttk.Frame(main_frame, style="TFrame")
    company_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(company_frame, text="Clave:", style="SubTitle.TLabel").grid(
        row=0, column=0, sticky=tk.W)
    entry_clave = ttk.Entry(company_frame, width=30)
    entry_clave.grid(row=0, column=1, sticky=tk.W, padx=(0, 10))
    ttk.Label(company_frame, text="Nombre:", style="SubTitle.TLabel").grid(
        row=1, column=0, sticky=tk.W)
    entry_nombre = ttk.Entry(company_frame, width=30)
    entry_nombre.grid(row=1, column=1, sticky=tk.W, padx=(0, 10))
    var_empresa_activa = tk.BooleanVar()
    ttk.Checkbutton(company_frame, text="Empresa Activa",
                    variable=var_empresa_activa).grid(row=2, column=0, sticky=tk.W)

    # Sección: Datos Facturación
    billing_frame = ttk.Frame(main_frame, style="TFrame")
    billing_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(billing_frame, text="Razón Social:",
              style="SubTitle.TLabel").grid(row=0, column=0, sticky=tk.W)
    entry_razon_social = ttk.Entry(billing_frame, width=30)
    entry_razon_social.grid(row=0, column=1, sticky=tk.W, padx=(0, 10))
    ttk.Label(billing_frame, text="RFC:", style="SubTitle.TLabel").grid(
        row=1, column=0, sticky=tk.W)
    entry_rfc = ttk.Entry(billing_frame, width=30)
    entry_rfc.grid(row=1, column=1, sticky=tk.W, padx=(0, 10))
    ttk.Label(billing_frame, text="Dirección:", style="SubTitle.TLabel").grid(
        row=2, column=0, sticky=tk.W)
    entry_direccion = ttk.Entry(billing_frame, width=30)
    entry_direccion.grid(row=2, column=1, sticky=tk.W, padx=(0, 10))

    # Sección: Datos Generales
    general_info_frame = ttk.Frame(main_frame, style="TFrame")
    general_info_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(general_info_frame, text="Nombre Ordenante:",
              style="SubTitle.TLabel").grid(row=0, column=0, sticky=tk.W)
    entry_nombre_ordenante = ttk.Entry(general_info_frame, width=30)
    entry_nombre_ordenante.grid(row=0, column=1, sticky=tk.W, padx=(0, 10))
    ttk.Label(general_info_frame, text="RFC Ordenante:",
              style="SubTitle.TLabel").grid(row=1, column=0, sticky=tk.W)
    entry_rfc_ordenante = ttk.Entry(general_info_frame, width=30)
    entry_rfc_ordenante.grid(row=1, column=1, sticky=tk.W, padx=(0, 10))

    # Botón de Aplicar
    ttk.Button(main_frame, text="Guardar", command=save_company).grid(
        row=3, column=0, sticky=tk.E, pady=20)

    root.mainloop()


if __name__ == "__main__":
    Nueva_Empresa()

import tkinter as tk
# from Nueva_Empresa import Nueva_Empresa  # Importa el archivo Nueva_Empresa.py
# from Pantallas.Lista_Empresas import Lista_Empresas # Importa el archivo Lista_Empresas.py
import subprocess


class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulación Sistema STP")
        self.geometry("800x600+150+10")
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

        # Limpia otras configuraciones previas si es necesario
        self.limpiar_configuracion()

        if opcion == "Propias":
            self.mostrar_propias()
        elif opcion == "Terceros":
            self.mostrar_terceros()
        elif opcion == "Manto. Cuenta Terceros":
            self.mostrar_manto_cuenta_terceros()

    # Funciones separadas para cada opción de 'Manto. Cuentas'
    def mostrar_propias(self):
        """Llama a la función 'Listas Empresas' del archivo Buscar_Empresas_Generales.py."""
        # Lista_Empresas()
        subprocess.Popen(["python", "Buscar_Empresas_Propias.py"])

    def mostrar_terceros(self):
        print("Mostrando configuración de cuentas de terceros...")
        # Aquí se puede agregar widgets específicos para 'Terceros'

    def mostrar_manto_cuenta_terceros(self):
        print("Mostrando configuración de mantenimiento de cuenta de terceros...")
        # Aquí se puede agregar widgets específicos para 'Manto. Cuenta Terceros'

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
        subprocess.Popen(["python", "Nueva_Empresa.py"])

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
        """Llama a la función 'Listas Empresas' del archivo Buscar_Empresas_Generales.py."""
        # Lista_Empresas()
        subprocess.Popen(["python", "Buscar_Empresas_Generales.py"])

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
        if self.boton_seleccionado_cuentas:
            try:
                self.boton_seleccionado_cuentas.config(bg='#d0cdc4')
            except tk.TclError:
                pass

        boton.config(bg='#b9b1ad')
        self.boton_seleccionado_cuentas = boton

        if opcion == "Procesos Automáticos":
            self.mostrar_procesos_automaticos()
        elif opcion == "Mensajes H2H":
            self.mostrar_mensajes_H2H()
        elif opcion == "Generales":
            self.mostrar_Generales_configuracion()
        elif opcion == "CEP":
            self.mostrar_CEP()

    def mostrar_procesos_automaticos(self):
        subprocess.Popen(["python", "Buscar_Empresas_Automaticos.py"])

    def mostrar_mensajes_H2H(self):
        print("Mostrando Mensajes H2H...")

    def mostrar_Generales_configuracion(self):
        subprocess.Popen(["python", "Buscar_Empresas_Varios_Generales.py"])

    def mostrar_CEP(self):
        subprocess.Popen(["python", "Buscar_Empresas_CEP.py"])

    def mostrar_folio_solicitud_CEP(self):
        print("Mostrando folio de solicitud CEP...")

    def mostrar_mensaje(self, mensaje):
        print(f"Mostrando {mensaje}...")

def main():
    app = Aplicacion()
    app.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import ttk
import mysql.connector


def Crear_Nueva_Cuenta(clave, prefijo):
    account_window = tk.Toplevel()
    account_window.title("Nueva Cuenta")
    account_window.configure(bg="#d9f0ff")

    main_frame = ttk.Frame(
        account_window, padding="15 15 15 15", style="Main.TFrame")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    main_frame.columnconfigure(0, weight=1)

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

    name_frame = ttk.Frame(main_frame, style="TFrame")
    name_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(name_frame, text="Nombre de la Cuenta",
              style="SubTitle.TLabel").grid(row=0, column=0, sticky=tk.W)
    account_name_entry = ttk.Entry(name_frame, width=30)
    account_name_entry.grid(row=1, column=0, sticky=tk.W, padx=(0, 10))

    account_number_frame = ttk.Frame(main_frame, style="TFrame")
    account_number_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(account_number_frame, text="Número de Cuenta",
              style="SubTitle.TLabel").grid(row=0, column=0, sticky=tk.W)
    ttk.Label(account_number_frame, text="Banco (3)").grid(
        row=1, column=0, sticky=tk.W)
    banco_entry = ttk.Entry(account_number_frame, width=5)
    banco_entry.grid(row=1, column=1, sticky=tk.W, padx=(0, 10))

    ttk.Label(account_number_frame, text="Plaza (3)").grid(
        row=2, column=0, sticky=tk.W)
    plaza_entry = ttk.Entry(account_number_frame, width=5)
    plaza_entry.grid(row=2, column=1, sticky=tk.W, padx=(0, 10))

    ttk.Label(account_number_frame, text="Prefijo (4)").grid(
        row=3, column=0, sticky=tk.W)
    # Cambiado para recibir el prefijo
    prefijo_entry = ttk.Entry(account_number_frame, width=5)
    prefijo_entry.grid(row=3, column=1, sticky=tk.W, padx=(0, 10))
    prefijo_entry.insert(0, prefijo)  # Muestra el prefijo actual

    ttk.Label(account_number_frame, text="Número (7)").grid(
        row=4, column=0, sticky=tk.W)
    numero_entry = ttk.Entry(account_number_frame, width=10)
    numero_entry.grid(row=4, column=1, sticky=tk.W, padx=(0, 10))

    ttk.Label(account_number_frame, text="DV (1)").grid(
        row=5, column=0, sticky=tk.W)
    dv_entry = ttk.Entry(account_number_frame, width=5)
    dv_entry.grid(row=5, column=1, sticky=tk.W, padx=(0, 10))

    ttk.Label(account_number_frame, text="Estado").grid(
        row=6, column=0, sticky=tk.W)
    state_combobox = ttk.Combobox(
        account_number_frame, values=["Activa", "Inactiva"])
    state_combobox.grid(row=6, column=1, sticky=tk.W)
    state_combobox.set("Activa")

    notification_frame = ttk.Frame(main_frame, style="TFrame")
    notification_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=5)
    notification_var = tk.BooleanVar()
    ttk.Checkbutton(notification_frame, text="Activar Notificación de Recepción de Abonos",
                    variable=notification_var).grid(row=0, column=0, sticky=tk.W)

    ttk.Button(main_frame, text="Aplicar", command=lambda: save_account(
        clave, account_name_entry.get(), banco_entry.get(), plaza_entry.get(), prefijo_entry.get(), numero_entry.get(), dv_entry.get(), state_combobox.get(), notification_var.get())).grid(row=3, column=0, sticky=tk.E, pady=20)


def save_account(clave, nombre_cuenta, numero_banco, plaza, prefijo, numero, dv, estado, notificacion):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sarinha_3",
        database="STP"
    )
    cursor = conn.cursor()

    insert_query = """INSERT INTO cuenta (clave, nombre_cuenta, numero_banco, plaza, prefijo, numero, dv, estado, notificacion_recibo_abonos)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(insert_query, (clave, nombre_cuenta, numero_banco,
                   plaza, prefijo, numero, dv, estado, notificacion))

    conn.commit()
    cursor.close()
    conn.close()

    print(f"Cuenta '{nombre_cuenta}' guardada.")


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter

    # Aquí se define cómo obtener 'clave' y 'prefijo'
    clave = "Josmar"  # Clave solo de muestra
    prefijo = "1"  # Pregijo solo de muestra

    Crear_Nueva_Cuenta(clave, prefijo)
    root.mainloop()

import sys
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from Crear_Nueva_Cuenta import Crear_Nueva_Cuenta


def Configuracion_Generales_Empresa(empresa_clave):
    root = tk.Tk()
    root.geometry("590x570+150+10")
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

import tkinter as tk
from tkinter import ttk
import mysql.connector
import sys


def main(clave):
    root = tk.Tk()
    root.title("Configuración de CEP")
    root.geometry("800x650+150+10")
    root.configure(bg="#d9f0ff")

    header_color = "#91ccea"
    section_color = "#bde0fe"

    header_frame = tk.Frame(root, bg="#d9f0ff")
    header_frame.pack(fill=tk.X, pady=(10, 10))

    header_label = tk.Label(header_frame, text="Configuración de CEP",
                            bg=header_color, fg="white", font=("Arial", 16))
    header_label.pack(side=tk.TOP, fill=tk.X)

    config_frame = tk.LabelFrame(
        root, text="Pagos válidos para CDA", bg=section_color, font=("Arial", 12), padx=10, pady=5)
    config_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    for col in range(3):
        config_frame.grid_columnconfigure(col, weight=1, uniform="col")
    config_frame.grid_columnconfigure(3, weight=2, uniform="col")

    def create_column_headers(frame):
        headers = ["Activar/Desactivar",
                   "Conf. Auto.", "Consulta", "Tipo de Pago"]
        for col, text in enumerate(headers):
            tk.Label(frame, text=text, bg=section_color, font=("Arial", 10, "bold")).grid(
                row=0, column=col, pady=2, padx=5, sticky="n")

    variables = {
        "Tercero": [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()],
        "TerceroVostro": [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()],
        "TerceroParticipante": [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()],
        "ParticipanteTercero": [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()],
        "ParticipanteVostro": [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()],
        "TerceroFSW": [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()],
        "TerceroVostroFSW": [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()],
        "ParticipanteFSW": [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()],
        "ParticipanteVostroFSW": [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()],
        "Nomina": [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()],
        "IndirectoTercero": [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()],
        "IndirectoParticipante": [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()],
        "PresencialUnaOcasión": [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()],
        "NoPresencialUnaOcasión": [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()],
        "NoPresencialRecurrente": [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()],
        "RemesaSaliente": [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()],
        "Otro": [tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()]
    }

    def create_option_row(frame, row, text, var_list):
        tk.Checkbutton(frame, variable=var_list[0], bg=section_color).grid(
            row=row, column=0, pady=2, padx=5, sticky="n")
        tk.Checkbutton(frame, variable=var_list[1], bg=section_color).grid(
            row=row, column=1, pady=2, padx=5, sticky="n")
        tk.Checkbutton(frame, variable=var_list[2], bg=section_color).grid(
            row=row, column=2, pady=2, padx=5, sticky="n")
        tk.Label(frame, text=text, bg=section_color).grid(
            row=row, column=3, pady=2, padx=5, sticky="w")

    create_column_headers(config_frame)

    for i, (key, var_list) in enumerate(variables.items(), start=1):
        create_option_row(config_frame, i, key.replace("_", " "), var_list)

    def insert_into_database():
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Sarinha_3",
                database="STP"
            )
            cursor = connection.cursor()

            sql_query = """
                INSERT INTO configuracion_cep (
                    clave,
                    Tercero_Activar, Tercero_Auto, Tercero_Consulta,
                    TerceroVostro_Activar, TerceroVostro_Auto, TerceroVostro_Consulta,
                    TerceroParticipante_Activar, TerceroParticipante_Auto, TerceroParticipante_Consulta,
                    ParticipanteTercero_Activar, ParticipanteTercero_Auto, ParticipanteTercero_Consulta,
                    ParticipanteVostro_Activar, ParticipanteVostro_Auto, ParticipanteVostro_Consulta,
                    TerceroFSW_Activar, TerceroFSW_Auto, TerceroFSW_Consulta,
                    TerceroVostroFSW_Activar, TerceroVostroFSW_Auto, TerceroVostroFSW_Consulta,
                    ParticipanteFSW_Activar, ParticipanteFSW_Auto, ParticipanteFSW_Consulta,
                    ParticipanteVostroFSW_Activar, ParticipanteVostroFSW_Auto, ParticipanteVostroFSW_Consulta,
                    Nomina_Activar, Nomina_Auto, Nomina_Consulta,
                    IndirectoTercero_Activar, IndirectoTercero_Auto, IndirectoTercero_Consulta,
                    IndirectoParticipante_Activar, IndirectoParticipante_Auto, IndirectoParticipante_Consulta,
                    PresencialUnaOcasión_Activar, PresencialUnaOcasión_Auto, PresencialUnaOcasión_Consulta,
                    NoPresencialUnaOcasión_Activar, NoPresencialUnaOcasión_Auto, NoPresencialUnaOcasión_Consulta,
                    NoPresencialRecurrente_Activar, NoPresencialRecurrente_Auto, NoPresencialRecurrente_Consulta,
                    RemesaSaliente_Activar, RemesaSaliente_Auto, RemesaSaliente_Consulta,
                    Otro_Activar, Otro_Auto, Otro_Consulta
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                )
            """

            data_values = [clave]
            for var_list in variables.values():
                data_values.extend([var.get() for var in var_list])

            cursor.execute(sql_query, data_values)
            connection.commit()
            print("Datos insertados correctamente en la base de datos.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    apply_button = tk.Button(
        root, text="Aplicar y Guardar en DB", bg=header_color, fg="white", font=("Arial", 12, "bold"), command=insert_into_database)
    apply_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        clave = sys.argv[1]  # Obtiene el argumento pasado
        main(clave)
    else:
        print("No se proporcionó ninguna clave.")

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
# from Configuracion_Generales import iniciar_configuracion
import subprocess


def Buscar_Empresas_Propias():
    clave = search_entry.get()

    try:
        # Conectar a la base de datos MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sarinha_3",
            database="STP"
        )
        cursor = conn.cursor()

        # Consulta para buscar la empresa por clave
        query = "SELECT * FROM empresa WHERE clave = %s"
        cursor.execute(query, (clave,))
        result = cursor.fetchone()

        if result:
            # Llamar a la función `Visualizar_Cuenta.py` pasando la clave de la empresa
            subprocess.Popen(["python", "Varios_Generales.py", clave])

        else:
            messagebox.showinfo(
                "Sin resultados", f"No se encontró ninguna empresa con la clave '{clave}'.")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al buscar la empresa: {err}")


def Buscar_Empresas():
    global search_entry
    root = tk.Tk()
    root.geometry("360x100+150+10")
    root.title("Buscar Empresa")
    root.configure(bg="#d9f0ff")

    main_frame = ttk.Frame(root, padding="15 15 15 15", style="Main.TFrame")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    main_frame.columnconfigure(0, weight=1)

    style = ttk.Style()
    style.configure("TLabel", background="#d9f0ff", font=("Arial", 10))
    style.configure("TButton", background="#d9f0ff")
    style.configure("Main.TFrame", background="#d9f0ff")
    style.configure("SubTitle.TLabel", font=(
        "Arial", 10, "bold"), background="#bde0fe")

    search_frame = ttk.Frame(main_frame, style="TFrame")
    search_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(search_frame, text="Clave de la Empresa:",
              style="SubTitle.TLabel").grid(row=0, column=0, sticky=tk.W)
    search_entry = ttk.Entry(search_frame, width=30)
    search_entry.grid(row=0, column=1, sticky=tk.W, padx=(0, 10))

    ttk.Button(search_frame, text="Buscar", command=Buscar_Empresas_Propias).grid(
        row=1, column=0, columnspan=2, pady=10)

    root.mainloop()


if __name__ == "__main__":
    Buscar_Empresas()

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
# from Configuracion_Generales import iniciar_configuracion
import subprocess


def Buscar_Empresas_Propias():
    clave = search_entry.get()

    try:
        # Conectar a la base de datos MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sarinha_3",
            database="STP"
        )
        cursor = conn.cursor()

        # Consulta para buscar la empresa por clave
        query = "SELECT * FROM empresa WHERE clave = %s"
        cursor.execute(query, (clave,))
        result = cursor.fetchone()

        if result:
            # Llamar a la función `Visualizar_Cuenta.py` pasando la clave de la empresa
            subprocess.Popen(["python", "Varios_Generales.py", clave])

        else:
            messagebox.showinfo(
                "Sin resultados", f"No se encontró ninguna empresa con la clave '{clave}'.")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al buscar la empresa: {err}")


def Buscar_Empresas():
    global search_entry
    root = tk.Tk()
    root.geometry("360x100+150+10")
    root.title("Buscar Empresa")
    root.configure(bg="#d9f0ff")

    main_frame = ttk.Frame(root, padding="15 15 15 15", style="Main.TFrame")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    main_frame.columnconfigure(0, weight=1)

    style = ttk.Style()
    style.configure("TLabel", background="#d9f0ff", font=("Arial", 10))
    style.configure("TButton", background="#d9f0ff")
    style.configure("Main.TFrame", background="#d9f0ff")
    style.configure("SubTitle.TLabel", font=(
        "Arial", 10, "bold"), background="#bde0fe")

    search_frame = ttk.Frame(main_frame, style="TFrame")
    search_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(search_frame, text="Clave de la Empresa:",
              style="SubTitle.TLabel").grid(row=0, column=0, sticky=tk.W)
    search_entry = ttk.Entry(search_frame, width=30)
    search_entry.grid(row=0, column=1, sticky=tk.W, padx=(0, 10))

    ttk.Button(search_frame, text="Buscar", command=Buscar_Empresas_Propias).grid(
        row=1, column=0, columnspan=2, pady=10)

    root.mainloop()


if __name__ == "__main__":
    Buscar_Empresas()

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
# from Configuracion_Generales import iniciar_configuracion
import subprocess


def Buscar_Empresas_Propias():
    clave = search_entry.get()

    try:
        # Conectar a la base de datos MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sarinha_3",
            database="STP"
        )
        cursor = conn.cursor()

        # Consulta para buscar la empresa por clave
        query = "SELECT * FROM empresa WHERE clave = %s"
        cursor.execute(query, (clave,))
        result = cursor.fetchone()

        if result:
            # Llamar a la función `Visualizar_Cuenta.py` pasando la clave de la empresa
            subprocess.Popen(["python", "Varios_Generales.py", clave])

        else:
            messagebox.showinfo(
                "Sin resultados", f"No se encontró ninguna empresa con la clave '{clave}'.")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al buscar la empresa: {err}")


def Buscar_Empresas():
    global search_entry
    root = tk.Tk()
    root.geometry("360x100+150+10")
    root.title("Buscar Empresa")
    root.configure(bg="#d9f0ff")

    main_frame = ttk.Frame(root, padding="15 15 15 15", style="Main.TFrame")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    main_frame.columnconfigure(0, weight=1)

    style = ttk.Style()
    style.configure("TLabel", background="#d9f0ff", font=("Arial", 10))
    style.configure("TButton", background="#d9f0ff")
    style.configure("Main.TFrame", background="#d9f0ff")
    style.configure("SubTitle.TLabel", font=(
        "Arial", 10, "bold"), background="#bde0fe")

    search_frame = ttk.Frame(main_frame, style="TFrame")
    search_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(search_frame, text="Clave de la Empresa:",
              style="SubTitle.TLabel").grid(row=0, column=0, sticky=tk.W)
    search_entry = ttk.Entry(search_frame, width=30)
    search_entry.grid(row=0, column=1, sticky=tk.W, padx=(0, 10))

    ttk.Button(search_frame, text="Buscar", command=Buscar_Empresas_Propias).grid(
        row=1, column=0, columnspan=2, pady=10)

    root.mainloop()


if __name__ == "__main__":
    Buscar_Empresas()

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
# from Configuracion_Generales import iniciar_configuracion
import subprocess


def Buscar_Empresas_Propias():
    clave = search_entry.get()

    try:
        # Conectar a la base de datos MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sarinha_3",
            database="STP"
        )
        cursor = conn.cursor()

        # Consulta para buscar la empresa por clave
        query = "SELECT * FROM empresa WHERE clave = %s"
        cursor.execute(query, (clave,))
        result = cursor.fetchone()

        if result:
            # Llamar a la función `Visualizar_Cuenta.py` pasando la clave de la empresa
            subprocess.Popen(["python", "Varios_Generales.py", clave])

        else:
            messagebox.showinfo(
                "Sin resultados", f"No se encontró ninguna empresa con la clave '{clave}'.")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al buscar la empresa: {err}")


def Buscar_Empresas():
    global search_entry
    root = tk.Tk()
    root.geometry("360x100+150+10")
    root.title("Buscar Empresa")
    root.configure(bg="#d9f0ff")

    main_frame = ttk.Frame(root, padding="15 15 15 15", style="Main.TFrame")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    main_frame.columnconfigure(0, weight=1)

    style = ttk.Style()
    style.configure("TLabel", background="#d9f0ff", font=("Arial", 10))
    style.configure("TButton", background="#d9f0ff")
    style.configure("Main.TFrame", background="#d9f0ff")
    style.configure("SubTitle.TLabel", font=(
        "Arial", 10, "bold"), background="#bde0fe")

    search_frame = ttk.Frame(main_frame, style="TFrame")
    search_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(search_frame, text="Clave de la Empresa:",
              style="SubTitle.TLabel").grid(row=0, column=0, sticky=tk.W)
    search_entry = ttk.Entry(search_frame, width=30)
    search_entry.grid(row=0, column=1, sticky=tk.W, padx=(0, 10))

    ttk.Button(search_frame, text="Buscar", command=Buscar_Empresas_Propias).grid(
        row=1, column=0, columnspan=2, pady=10)

    root.mainloop()


if __name__ == "__main__":
    Buscar_Empresas()
