from flask import Flask
from src.views.home_view import home_bp

app = Flask(__name__, template_folder='resources/templates')

# Registrar blueprint
app.register_blueprint(home_bp)

if __name__ == '__main__':
    app.run(debug=True)