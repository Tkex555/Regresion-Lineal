import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
from ..models.model import RegresionLinealModelo

class ViviendaController:
    def __init__(self, ruta_excel):
        self.df = pd.read_excel(ruta_excel)
        self.modelo = RegresionLinealModelo(self.df)

    def mostrar_tabla(self):
        print(tabulate(self.df, headers='keys', tablefmt='psql'))

    def resumen_estadistico(self):
        total = len(self.df)
        self.df['precio_m2'] = self.df['precio'] / self.df['area']
        promedio = self.df['precio_m2'].mean()
        print(f"Total de viviendas: {total}")
        print(f"Promedio precio por m2: {promedio:.2f}")
        if 'tipo' in self.df.columns:
            print(self.df['tipo'].value_counts())
        else:
            print("No hay columna 'tipo' en el dataset.")