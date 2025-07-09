from pymongo import MongoClient

class MongoConexion:
    def __init__(self, host="localhost", puerto=27017, db_name="Viviendas"):
        self.host = host
        self.puerto = puerto
        self.db_name = db_name
        self.cliente = None
        self.db = None

    def conectar(self):
        try:
            self.cliente = MongoClient(f"{self.host}:{self.puerto}", serverSelectionTimeoutMS=5000)
            self.db = self.cliente[self.db_name]
            self.cliente.server_info()
            print("Conexión exitosa a MongoDB. Listo para usar.")
        except Exception as e:
            print(f"Error al conectar a MongoDB: {e}")

    def obtener_db(self):
        if self.db is None:
            raise Exception("No se ha establecido una conexión a la base de datos.")
        return self.db


if __name__ == "__main__":
    conexion = MongoConexion()
    conexion.conectar()
