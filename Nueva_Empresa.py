import tkinter as tk
from tkinter import ttk


def new_company_interface():
    root = tk.Tk()
    root.title("Nueva Empresa")
    root.configure(bg="#d9f0ff")  # Fondo azul pastel claro para la ventana

    # Main Frame con diseño y color de fondo azul pastel
    main_frame = ttk.Frame(root, padding="15 15 15 15", style="Main.TFrame")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    main_frame.columnconfigure(0, weight=1)

    # Estilos de colores
    style = ttk.Style()
    style.configure("TLabel", background="#d9f0ff", font=("Arial", 10))
    style.configure("TCheckbutton", background="#d9f0ff")
    style.configure("Main.TFrame", background="#d9f0ff")
    style.configure("Title.TLabel", font=(
        "Arial", 12, "bold"), background="#91ccea")
    style.configure("SubTitle.TLabel", font=(
        "Arial", 10, "bold"), background="#bde0fe")
    style.configure("TFrame", background="#bde0fe",
                    padding="10 10 10 10", relief="groove", borderwidth=2)

    # Sección: Empresa
    company_frame = ttk.Frame(main_frame, style="TFrame")
    company_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(company_frame, text="Clave:", style="SubTitle.TLabel").grid(
        row=0, column=0, sticky=tk.W)
    ttk.Entry(company_frame, width=30).grid(
        row=0, column=1, sticky=tk.W, padx=(0, 10))
    ttk.Label(company_frame, text="Nombre:", style="SubTitle.TLabel").grid(
        row=1, column=0, sticky=tk.W)
    ttk.Entry(company_frame, width=30).grid(
        row=1, column=1, sticky=tk.W, padx=(0, 10))
    ttk.Checkbutton(company_frame, text="Empresa Activa").grid(
        row=2, column=0, sticky=tk.W)

    # Sección: Datos Facturación
    billing_frame = ttk.Frame(main_frame, style="TFrame")
    billing_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(billing_frame, text="Razón Social:",
              style="SubTitle.TLabel").grid(row=0, column=0, sticky=tk.W)
    ttk.Entry(billing_frame, width=30).grid(
        row=0, column=1, sticky=tk.W, padx=(0, 10))
    ttk.Label(billing_frame, text="RFC:", style="SubTitle.TLabel").grid(
        row=1, column=0, sticky=tk.W)
    ttk.Entry(billing_frame, width=30).grid(
        row=1, column=1, sticky=tk.W, padx=(0, 10))
    ttk.Label(billing_frame, text="Dirección:", style="SubTitle.TLabel").grid(
        row=2, column=0, sticky=tk.W)
    ttk.Entry(billing_frame, width=30).grid(
        row=2, column=1, sticky=tk.W, padx=(0, 10))

    # Sección: Datos Generales
    general_info_frame = ttk.Frame(main_frame, style="TFrame")
    general_info_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=5)
    ttk.Label(general_info_frame, text="Nombre Ordenante:",
              style="SubTitle.TLabel").grid(row=0, column=0, sticky=tk.W)
    ttk.Entry(general_info_frame, width=30).grid(
        row=0, column=1, sticky=tk.W, padx=(0, 10))
    ttk.Label(general_info_frame, text="RFC Ordenante:",
              style="SubTitle.TLabel").grid(row=1, column=0, sticky=tk.W)
    ttk.Entry(general_info_frame, width=30).grid(
        row=1, column=1, sticky=tk.W, padx=(0, 10))

    # Botón de Aplicar
    ttk.Button(main_frame, text="Aplicar", command=lambda: save_company()).grid(
        row=3, column=0, sticky=tk.E, pady=20)


def save_company():
    # Aquí va la lógica para guardar la empresa
    print("Empresa guardada.")


if __name__ == "__main__":
    new_company_interface()
    tk.mainloop()
