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

    def diagrama_dispersion(self):
        plt.scatter(self.df['area'], self.df['precio'])
        plt.xlabel('Área (m2)')
        plt.ylabel('Precio')
        plt.title('Área vs Precio')
        plt.show()

    def entrenar_y_graficar_regresion(self):
        intercepto, pendiente = self.modelo.entrenar()
        X = self.df[['area']]
        y = self.df['precio']
        y_pred = self.modelo.modelo.predict(X)
        plt.scatter(self.df['area'], self.df['precio'], label='Datos reales')
        plt.plot(self.df['area'], y_pred, color='red', label='Regresión lineal')
        plt.xlabel('Área (m2)')
        plt.ylabel('Precio')
        plt.title('Regresión lineal: área vs precio')
        plt.legend()
        plt.show()
        print(f"Intercepto: {intercepto}")
        print(f"Pendiente: {pendiente}")
        mse, r2 = self.modelo.obtener_metricas()
        print(f"MSE: {mse}")
        print(f"R²: {r2}")