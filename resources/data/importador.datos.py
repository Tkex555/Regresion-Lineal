import pandas as pd
from pymongo import MongoClient
import os
import re

def detectar_tipo(descripcion):
    if not isinstance(descripcion, str):
        return "Otro"
    desc = descripcion.lower()
    if "casa" in desc:
        return "Casa"
    elif "apartamento" in desc:
        return "Apartamento"
    else:
        return "Otro"

def obtener_id_tipo(nombre_tipo, db):
    tipo = db["tipo_vivienda"].find_one({"nombre": nombre_tipo})
    return tipo["_id"] if tipo else None

def cargar_dataset_y_obtener_datos(ruta_archivo, nombre_db, nombre_coleccion):
    df = pd.read_excel(ruta_archivo)
    datos = df.to_dict(orient='records')

    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente[nombre_db]
    coleccion = db[nombre_coleccion]
    coleccion.delete_many({})

    viviendas_con_tipo = []
    for vivienda in datos:
        tipo_detectado = detectar_tipo(vivienda.get("descripcion", ""))
        id_tipo = obtener_id_tipo(tipo_detectado, db)
        vivienda["id_tipo_vivienda"] = id_tipo
        viviendas_con_tipo.append(vivienda)

    coleccion.insert_many(viviendas_con_tipo)
    print(f"Se importaron {len(viviendas_con_tipo)} registros a la colección '{nombre_coleccion}' en la base de datos '{nombre_db}'.")
    return pd.DataFrame(viviendas_con_tipo)

ruta_base = os.path.dirname(os.path.abspath(__file__))
archivo = os.path.join(ruta_base, "dataset_vivienda.xlsx")
base_datos = "Viviendas"
coleccion = "vivienda"

df = cargar_dataset_y_obtener_datos(archivo, base_datos, coleccion)
print(df.head())
