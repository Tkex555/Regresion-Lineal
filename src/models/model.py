from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

class RegresionLinealModelo:
    def __init__(self, df):
        self.df = df
        self.modelo = LinearRegression()
        self.entrenado = False

    def entrenar(self):
        X = self.df[['area']]
        y = self.df['precio']
        self.modelo.fit(X, y)
        self.entrenado = True
        intercepto = self.modelo.intercept_
        pendiente = self.modelo.coef_[0]
        return intercepto, pendiente

    def predecir(self, area):
        if not self.entrenado:
            raise Exception("El modelo no ha sido entrenado.")
        return self.modelo.predict([[area]])[0]

    def obtener_metricas(self):
        if not self.entrenado:
            raise Exception("El modelo no ha sido entrenado.")
        X = self.df[['area']]
        y = self.df['precio']
        y_pred = self.modelo.predict(X)
        mse = mean_squared_error(y, y_pred)
        r2 = r2_score(y, y_pred)
        return mse, r2