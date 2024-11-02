import tkinter as tk
from tkinter import ttk


def create_account_interface():
    account_window = tk.Toplevel()
    account_window.title("Nueva Cuenta")
    # Fondo azul pastel claro para la ventana
    account_window.configure(bg="#d9f0ff")

    # Main Frame con diseño y color de fondo azul pastel
    main_frame = ttk.Frame(
        account_window, padding="15 15 15 15", style="Main.TFrame")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    main_frame.columnconfigure(0, weight=1)

    # Estilos de colores
    style = ttk.Style()
    style.configure("TLabel", background="#d9f0ff", font=("Arial", 10))
    style.configure("TCheckbutton", background="#d9f0ff")
    style.configure("TRadiobutton", background="#d9f0ff")
    style.configure("Main.TFrame", background="#d9f0ff")
    # Fondo azul pastel más oscuro para títulos
    style.configure("Title.TLabel", font=(
        "Arial", 12, "bold"), background="#91ccea")
    style.configure("SubTitle.TLabel", font=(
        "Arial", 10, "bold"), background="#bde0fe")
    style.configure("TFrame", background="#bde0fe",
                    padding="10 10 10 10", relief="groove", borderwidth=2)

    # Sección: Nombre de la cuenta
    name_frame = ttk.Frame(main_frame, style="TFrame")
    name_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(name_frame, text="Nombre de la Cuenta",
              style="SubTitle.TLabel").grid(row=0, column=0, sticky=tk.W)
    account_name_entry = ttk.Entry(name_frame, width=30)
    account_name_entry.grid(row=1, column=0, sticky=tk.W, padx=(0, 10))
    account_name_entry.insert(0, "")

    # Sección: Número de Cuenta
    account_number_frame = ttk.Frame(main_frame, style="TFrame")
    account_number_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(account_number_frame, text="Número de Cuenta",
              style="SubTitle.TLabel").grid(row=0, column=0, sticky=tk.W)
    ttk.Label(account_number_frame, text="Banco (3)").grid(
        row=1, column=0, sticky=tk.W)
    ttk.Entry(account_number_frame, width=5).grid(
        row=1, column=1, sticky=tk.W, padx=(0, 10))
    ttk.Label(account_number_frame, text="Plaza (3)").grid(
        row=2, column=0, sticky=tk.W)
    ttk.Entry(account_number_frame, width=5).grid(
        row=2, column=1, sticky=tk.W, padx=(0, 10))
    ttk.Label(account_number_frame, text="Prefijo (4)").grid(
        row=3, column=0, sticky=tk.W)
    ttk.Entry(account_number_frame, width=5).grid(
        row=3, column=1, sticky=tk.W, padx=(0, 10))
    ttk.Label(account_number_frame, text="Número (7)").grid(
        row=4, column=0, sticky=tk.W)
    ttk.Entry(account_number_frame, width=10).grid(
        row=4, column=1, sticky=tk.W, padx=(0, 10))
    ttk.Label(account_number_frame, text="DV (1)").grid(
        row=5, column=0, sticky=tk.W)
    ttk.Entry(account_number_frame, width=5).grid(
        row=5, column=1, sticky=tk.W, padx=(0, 10))
    ttk.Label(account_number_frame, text="Estado").grid(
        row=6, column=0, sticky=tk.W)
    state_combobox = ttk.Combobox(
        account_number_frame, values=["Activa", "Inactiva"])
    state_combobox.grid(row=6, column=1, sticky=tk.W)
    state_combobox.set("Activa")

    # Sección: Notificación de Recepción de Abonos
    notification_frame = ttk.Frame(main_frame, style="TFrame")
    notification_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Checkbutton(notification_frame, text="Activar Notificación de Recepción de Abonos").grid(
        row=0, column=0, sticky=tk.W)

    # Botón de Aplicar
    ttk.Button(main_frame, text="Aplicar", command=lambda: save_account(
        account_name_entry.get())).grid(row=3, column=0, sticky=tk.E, pady=20)


def save_account(account_name):
    # Aquí va la lógica para guardar la cuenta
    print(f"Cuenta '{account_name}' guardada.")


if __name__ == "__main__":
    create_account_interface()
