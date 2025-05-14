import tkinter as tk
from tkinter import messagebox

class GestionCamaras:
    def __init__(self, parent, db):
        self.parent = parent
        self.db = db
        self.window = tk.Toplevel(self.parent)
        self.window.title("Gestión de Cámaras")
        self.window.geometry("400x300")

        # Campo para agregar cámaras
        tk.Label(self.window, text="Nombre de la Cámara:").pack(pady=5)
        self.entry_nombre_camara = tk.Entry(self.window)
        self.entry_nombre_camara.pack(pady=5)

        self.btn_agregar = tk.Button(self.window, text="Agregar Cámara", command=self.agregar_camara)
        self.btn_agregar.pack(pady=5)

        # Lista de cámaras
        tk.Label(self.window, text="Cámaras Disponibles:").pack(pady=5)
        self.lista_camaras = tk.Listbox(self.window)
        self.lista_camaras.pack(fill=tk.BOTH, expand=True, pady=5)

        self.btn_eliminar = tk.Button(self.window, text="Eliminar Cámara", command=self.eliminar_camara)
        self.btn_eliminar.pack(pady=5)

        self.cargar_camaras()

    def agregar_camara(self):
        nombre = self.entry_nombre_camara.get()
        if nombre:
            self.db.agregar_camara(nombre)
            self.entry_nombre_camara.delete(0, tk.END)
            self.cargar_camaras()
            messagebox.showinfo("Éxito", f"Cámara '{nombre}' agregada correctamente.")
        else:
            messagebox.showerror("Error", "El nombre de la cámara no puede estar vacío.")

    def eliminar_camara(self):
        seleccion = self.lista_camaras.curselection()
        if seleccion:
            nombre = self.lista_camaras.get(seleccion)
            self.db.cursor.execute("DELETE FROM Camaras WHERE nombre = ?", (nombre,))
            self.db.conn.commit()
            self.cargar_camaras()
            messagebox.showinfo("Éxito", f"Cámara '{nombre}' eliminada correctamente.")
        else:
            messagebox.showerror("Error", "Debe seleccionar una cámara para eliminar.")

    def cargar_camaras(self):
        self.lista_camaras.delete(0, tk.END)
        camaras = self.db.cursor.execute("SELECT nombre FROM Camaras").fetchall()
        for camara in camaras:
            self.lista_camaras.insert(tk.END, camara[0])
