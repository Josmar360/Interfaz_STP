import tkinter as tk
from tkinter import ttk
import mysql.connector


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
    root = tk.Tk()
    root.withdraw()  # Ocultamos la ventana principal de Tkinter

    # Aquí debes definir cómo obtener 'clave'
    clave = "Josmar"  # Cambia esto según tu lógica

    Crear_Nueva_Cuenta(clave)
    root.mainloop()
