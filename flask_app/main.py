from flask import Flask
from flask_migrate import Migrate
from flask_app.config.config import Config
from flask_app.models.session import db
from flask_app.routes.routes import obtener_clientes, agregar_cliente, obtener_cliente, actualizar_cliente

app = Flask(__name__, static_folder='frontend/static')

# clientes GET routes
app.add_url_rule('/api/clientes', view_func=obtener_clientes, methods=['GET'])
app.add_url_rule('/api/clientes/<int:id>', view_func=obtener_cliente, methods=['GET'])

# clientes POST routes
app.add_url_rule('/api/clientes', view_func=agregar_cliente, methods=['POST'])
app.add_url_rule('/api/clientes/<int:id>', view_func=actualizar_cliente, methods=['PUT'])

app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True)
