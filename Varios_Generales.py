import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  # Asegúrate de importar messagebox
import mysql.connector  # Asegúrate de que esta librería está instalada
import sys

def create_config_window(clave):
    root = tk.Tk()
    root.title("Configuración")
    root.geometry("500x670+300+50")
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
                host='localhost',          # Cambia por tu host
                user='root',       # Cambia por tu usuario
                password='Sarinha_3',  # Cambia por tu contraseña
                database='STP'  # Cambia por tu base de datos
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
            root.destroy()  # Cerrar la ventana después de guardar

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