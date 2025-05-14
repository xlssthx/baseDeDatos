import tkinter as tk

class SistemaSeguridadVista:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Seguridad")
        self.root.geometry("600x400")

        # Título
        tk.Label(root, text="Sistema de Seguridad con Cámaras", font=("Arial", 16, "bold")).pack(pady=10)

        # Botones de navegación
        tk.Button(root, text="Gestión de Cámaras", command=self.gestionar_camaras).pack(pady=5)
        tk.Button(root, text="Historial de Alertas", command=self.ver_historial_alertas).pack(pady=5)

    # Métodos para los botones (serán conectados desde el controlador)
    gestionar_camaras = None
    ver_historial_alertas = None
