from flask import Flask
from flask_migrate import Migrate
from flask_app.config.config import Config
from flask_app.models.session import db
from flask_app.routes.routes import obtener_clientes, agregar_cliente, obtener_cliente, actualizar_cliente, \
    eliminar_cliente

from flask_app.routes.routes_componentes import obtener_componentes, agregar_componente, obtener_componente, \
    actualizar_componente, eliminar_componente

app = Flask(__name__, static_folder='frontend/static')

# clientes GET routes
app.add_url_rule('/api/clientes', view_func=obtener_clientes, methods=['GET'])
app.add_url_rule('/api/clientes/<int:id>', view_func=obtener_cliente, methods=['GET'])

# clientes POST / PUT routes
app.add_url_rule('/api/clientes', view_func=agregar_cliente, methods=['POST'])
app.add_url_rule('/api/clientes/<int:id>', view_func=actualizar_cliente, methods=['PUT'])

# clientes DELETE routes
app.add_url_rule('/api/clientes/<int:id>', view_func=eliminar_cliente, methods=['DELETE'])

# componentes GET routes
app.add_url_rule('/api/componentes', view_func=obtener_componentes, methods=['GET'])
app.add_url_rule('/api/componentes/<int:id>', view_func=obtener_componente, methods=['GET'])

# componentes POST / PUT routes
app.add_url_rule('/api/componentes', view_func=agregar_componente, methods=['POST'])
app.add_url_rule('/api/componentes/<int:id>', view_func=actualizar_componente, methods=['PUT'])

# componentes DELETE routes
app.add_url_rule('/api/componentes/<int:id>', view_func=eliminar_componente, methods=['DELETE'])

app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True)
