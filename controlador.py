from vista import SistemaSeguridadVista
from database_integration import SistemaSeguridadDB
from vista_camaras import GestionCamaras
from vista_alertas import HistorialAlertas

class SistemaSeguridadControlador:
    def __init__(self, root):
        self.db = SistemaSeguridadDB()
        self.vista = SistemaSeguridadVista(root)

        # Conectar eventos
        self.vista.gestionar_camaras = self.abrir_gestion_camaras
        self.vista.ver_historial_alertas = self.abrir_historial_alertas

    def abrir_gestion_camaras(self):
        GestionCamaras(self.vista.root, self.db)

    def abrir_historial_alertas(self):
        HistorialAlertas(self.vista.root, self.db)
