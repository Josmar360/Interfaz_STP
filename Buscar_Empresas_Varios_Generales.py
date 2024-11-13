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
