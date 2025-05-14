import tkinter as tk
from controlador import SistemaSeguridadControlador

if __name__ == "__main__":
    # Crear la ventana principal
    root = tk.Tk()
    # Iniciar el controlador principal
    app = SistemaSeguridadControlador(root)
    root.mainloop()
