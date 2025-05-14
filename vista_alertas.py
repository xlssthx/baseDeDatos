import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class HistorialAlertas:
    def __init__(self, parent, db):
        self.parent = parent
        self.db = db
        self.window = tk.Toplevel(self.parent)
        self.window.title("Historial de Alertas")
        self.window.geometry("600x400")

        # Tabla para mostrar alertas
        self.tree = ttk.Treeview(self.window, columns=("ID", "Cámara", "Tipo", "Fecha/Hora", "Revisada"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Cámara", text="Cámara")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Fecha/Hora", text="Fecha/Hora")
        self.tree.heading("Revisada", text="Revisada")
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)

        # Botón para marcar como revisada
        self.btn_revisar = tk.Button(self.window, text="Marcar como Revisada", command=self.marcar_revisada)
        self.btn_revisar.pack(pady=5)

        self.cargar_alertas()

    def cargar_alertas(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        alertas = self.db.obtener_historial_alertas()
        for alerta in alertas:
            self.tree.insert("", tk.END, values=(alerta[0], alerta[1], alerta[2], alerta[3], "Sí" if alerta[4] else "No"))

    def marcar_revisada(self):
        seleccion = self.tree.selection()
        if seleccion:
            id_alerta = self.tree.item(seleccion)["values"][0]
            self.db.marcar_alerta_revisada(id_alerta)
            self.cargar_alertas()
            messagebox.showinfo("Éxito", f"Alerta con ID {id_alerta} marcada como revisada.")
        else:
            messagebox.showerror("Error", "Debe seleccionar una alerta para marcar como revisada.")
