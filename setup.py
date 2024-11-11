from setuptools import setup

setup(
    name="Simulacion STP", 
    version="1.0.0",
    py_modules=[
        "Buscar_Empresas_Automaticos",
        "Buscar_Empresas_CEP",
        "Buscar_Empresas_Generales",
        "Buscar_Empresas_Propias",
        "Buscar_Empresas_Varios_Generales",
        "Configuracion_CEP",
        "Configuracion_Generales",
        "Crear_Nueva_Cuenta",
        "Funciones",
        "Menu_Principal",
        "Nueva_Empresa",
        "Procesos_Automaticos",
        "Varios_Generales",
        "Visualizar_Cuenta"
    ],
    install_requires=[
        "mysql-connector-python"
    ],
    entry_points={
        'console_scripts': [
            'simulacion_stp=Menu_Principal:main'  
        ]
    },
    author="Josmar Gustavo Palomino Castelan",
    author_email="josmargustavopalominocastelan@gmail.com",
    description="Este proyecto es una simulación del flujo de pantallas que tiene el sistema STP, para ahcer una demostración de Automation Anywhere",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Josmar360/Interfaz_STP",
)
