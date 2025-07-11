from flask import Flask
from src.views.home_view import home_bp

app = Flask(__name__, template_folder='resources/templates', static_folder='resources/static')

# Registrar blueprint
app.register_blueprint(home_bp)

if __name__ == '__main__':
    from src.controllers.controller import ViviendaController
    print("\n--- RESUMEN ESTADÍSTICO ---")
    controlador = ViviendaController()
    controlador.resumen_estadistico()
    app.run(debug=True)