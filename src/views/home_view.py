from flask import Blueprint, render_template
from src.controllers.controller import ViviendaController

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    # Supón que tienes un archivo Excel o puedes adaptar para MongoDB
    controller = ViviendaController()  # Sin argumentos, usa MongoDB
    viviendas = controller.df.to_dict(orient='records')
    return render_template('home.html', viviendas=viviendas)