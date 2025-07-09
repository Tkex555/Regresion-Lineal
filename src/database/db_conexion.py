from pymongo import MongoClient

try:
    cliente = MongoClient("localhost:27017", serverSelectionTimeoutMS=5000)
    db = cliente["Viviendas"]
    cliente.server_info()
    print("Conexión exitosa a MongoDB y acceso a la base de datos.")
except Exception as e:
    print(f"Error al conectar a MongoDB: {e}")
