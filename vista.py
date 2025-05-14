import tkinter as tk

class SistemaSeguridadVista:
    def __init__(self, root, gestionar_camaras_callback, ver_historial_alertas_callback):
        self.root = root
        self.root.title("Sistema de Seguridad")
        self.root.geometry("600x400")

        # Título
        tk.Label(root, text="Sistema de Seguridad con Cámaras", font=("Arial", 16, "bold")).pack(pady=10)

        # Botones de navegación
        tk.Button(root, text="Gestión de Cámaras", command=gestionar_camaras_callback).pack(pady=5)
        tk.Button(root, text="Historial de Alertas", command=ver_historial_alertas_callback).pack(pady=5)

