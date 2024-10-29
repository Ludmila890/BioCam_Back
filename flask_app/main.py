from flask import Flask
from flask_migrate import Migrate
from flask_app.config.config import Config
from flask_app.models.session import db
from flask_app.routes.routes_clientes import obtener_clientes, agregar_cliente, obtener_cliente, actualizar_cliente, \
    eliminar_cliente

from flask_app.routes.routes_componentes import obtener_componentes, agregar_componente, obtener_componente, \
    actualizar_componente, eliminar_componente

from flask_app.routes.routes_carrito import obtener_carritos, agregar_carrito

app = Flask(__name__, static_folder='frontend/static')

# GET routes
# Clientes
app.add_url_rule('/api/clientes', view_func=obtener_clientes, methods=['GET'])
app.add_url_rule('/api/clientes/<int:id>', view_func=obtener_cliente, methods=['GET'])

# Componentes
app.add_url_rule('/api/componentes', view_func=obtener_componentes, methods=['GET'])
app.add_url_rule('/api/componentes/<int:id>', view_func=obtener_componente, methods=['GET'])

# Carrito
app.add_url_rule('/api/carritos', view_func=obtener_carritos, methods=['GET'])
# app.add_url_rule('/api/carritos/<int:id>', view_func=obtener_carrito, methods=['GET'])


# POST / PUT routes
# Clientes
app.add_url_rule('/api/clientes', view_func=agregar_cliente, methods=['POST'])
app.add_url_rule('/api/clientes/<int:id>', view_func=actualizar_cliente, methods=['PUT'])

# Componentes
app.add_url_rule('/api/componentes', view_func=agregar_componente, methods=['POST'])
app.add_url_rule('/api/componentes/<int:id>', view_func=actualizar_componente, methods=['PUT'])

# Carrito
app.add_url_rule('/api/carritos', view_func=agregar_carrito, methods=['POST'])


# DELETE routes
# Clientes
app.add_url_rule('/api/clientes/<int:id>', view_func=eliminar_cliente, methods=['DELETE'])

# Componentes
app.add_url_rule('/api/componentes/<int:id>', view_func=eliminar_componente, methods=['DELETE'])

# Carrito


app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True)
