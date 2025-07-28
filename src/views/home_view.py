from flask import Blueprint, render_template, Response
from src.controllers.controller import ViviendaController
import io
import matplotlib.pyplot as plt
import base64

# 🔸 Primero defines el Blueprint
home_bp = Blueprint('home', __name__)

# 🔸 Luego defines la ruta
@home_bp.route('/')
def index():
    controller = ViviendaController()
    viviendas = controller.df.to_dict(orient='records')

    total = len(controller.df)
    controller.df['precio_m2'] = controller.df['precio'] / controller.df['area']
    promedio = controller.df['precio_m2'].mean()
    tipos = controller.df['tipo'].value_counts().to_dict() if 'tipo' in controller.df.columns else {}

    resumen = f"Total de viviendas en el sistema: {total}\n"
    resumen += f"Promedio del precio por metro cuadrado de la vivienda en la región: ${promedio:,.2f}\n"
    resumen += "Clasificación y total de viviendas por tipo de vivienda:\n"
    for tipo, cantidad in tipos.items():
        resumen += f"- {tipo}: {cantidad}\n"

    return render_template('home.html', viviendas=viviendas, total=total, promedio=promedio, tipos=tipos, resumen=resumen)

@home_bp.route('/diagrama')
def diagrama():
    controller = ViviendaController()
    fig, ax = plt.subplots()
    # Puntos
    ax.scatter(controller.df['area'], controller.df['precio'], label='Datos reales')
    # Línea de regresión
    controller.modelo.entrenar()
    X = controller.df[['area']]
    y_pred = controller.modelo.modelo.predict(X)
    ax.plot(controller.df['area'], y_pred, color='red', label='Regresión lineal')
    # Cuadrícula
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_xlabel('Área (m2)')
    ax.set_ylabel('Precio')
    ax.set_title('Área vs Precio')
    ax.legend()
    import io, base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    return render_template('diagrama.html', image_base64=image_base64)

@home_bp.route('/predecir', methods=['GET', 'POST'])
def predecir():
    prediccion = None
    if request.method == 'POST':
        area = float(request.form['area'])
        habitaciones = int(request.form['habitaciones'])
        antiguedad = int(request.form['antiguedad'])

        controller = ViviendaController()
        controller.modelo.entrenar()
        prediccion = controller.modelo.predecir(area, habitaciones, antiguedad)

    return render_template('predecir.html', prediccion=prediccion)

