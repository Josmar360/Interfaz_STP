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