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
