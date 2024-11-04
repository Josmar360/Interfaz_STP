import tkinter as tk
from tkinter import ttk
import mysql.connector


def main(clave):
    root = tk.Tk()
    root.title("Configuración de CEP")
    root.geometry("800x650+300+50")
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
    main("Prueba1")
