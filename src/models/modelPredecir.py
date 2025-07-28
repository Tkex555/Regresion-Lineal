from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

class RegresionLinealModelo:
    def __init__(self, df):
        self.df = df
        self.modelo = LinearRegression()
        self.entrenado = False

    def entrenar(self):
        # Entrenamos con las tres variables: área, habitaciones y antigüedad
        X = self.df[['area', 'habitaciones', 'antiguedad']]
        y = self.df['precio']
        self.modelo.fit(X, y)
        self.entrenado = True
        return self.modelo.intercept_, self.modelo.coef_

    def predecir(self, area, habitaciones, antiguedad):
        if not self.entrenado:
            raise Exception("El modelo no ha sido entrenado.")
        # Crear el vector de entrada con las tres variables
        entrada = np.array([[area, habitaciones, antiguedad]])
        return self.modelo.predict(entrada)[0]

    def obtener_metricas(self):
        if not self.entrenado:
            raise Exception("El modelo no ha sido entrenado.")
        X = self.df[['area', 'habitaciones', 'antiguedad']]
        y = self.df['precio']
        y_pred = self.modelo.predict(X)
        mse = mean_squared_error(y, y_pred)
        r2 = r2_score(y, y_pred)
        return mse, r2
