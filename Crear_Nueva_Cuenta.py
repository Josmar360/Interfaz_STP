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
