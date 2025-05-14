import sqlite3

class SistemaSeguridadDB:
    def __init__(self, db_name="seguridad.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Camaras (
                id_camara INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                estado TEXT DEFAULT 'Inactiva'
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Alertas (
                id_alerta INTEGER PRIMARY KEY AUTOINCREMENT,
                id_camara INTEGER,
                tipo_alerta TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                revisada BOOLEAN DEFAULT 0,
                FOREIGN KEY (id_camara) REFERENCES Camaras(id_camara)
            )
        ''')
        self.conn.commit()

    def agregar_camara(self, nombre):
        self.cursor.execute('INSERT INTO Camaras (nombre) VALUES (?)', (nombre,))
        self.conn.commit()
    
    def registrar_alerta(self, id_camara, tipo_alerta):
        self.cursor.execute('INSERT INTO Alertas (id_camara, tipo_alerta) VALUES (?, ?)', (id_camara, tipo_alerta))
        self.conn.commit()

    def obtener_historial_alertas(self):
        self.cursor.execute('SELECT * FROM Alertas ORDER BY timestamp DESC')
        return self.cursor.fetchall()

    def marcar_alerta_revisada(self, id_alerta):
        self.cursor.execute('UPDATE Alertas SET revisada = 1 WHERE id_alerta = ?', (id_alerta,))
        self.conn.commit()

    def cerrar_conexion(self):
        self.conn.close()
