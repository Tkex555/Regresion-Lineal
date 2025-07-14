import pandas as pd
from pymongo import MongoClient
import os

def cargar_dataset_y_obtener_datos(ruta_archivo, nombre_db, nombre_coleccion):
    df = pd.read_excel(ruta_archivo)
    datos = df.to_dict(orient='records')
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente[nombre_db]
    coleccion = db[nombre_coleccion]
    coleccion.delete_many({})
    coleccion.insert_many(datos)
    print(f"Se importaron {len(datos)} registros a la colección '{nombre_coleccion}' en la base de datos '{nombre_db}'.")
    return df

ruta_base = os.path.dirname(os.path.abspath(__file__))
archivo = os.path.join(ruta_base, "dataset_vivienda.xlsx")
base_datos = "Viviendas"
coleccion = "vivienda"

df = cargar_dataset_y_obtener_datos(archivo, base_datos, coleccion)
print(df.head())
