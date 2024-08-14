from flask import Blueprint, render_template

from views.cliente_view import cliente_blueprint
from views.produto_view import produto_blueprint

root_blueprint = Blueprint('root', __name__)

root_blueprint.register_blueprint(produto_blueprint)
root_blueprint.register_blueprint(cliente_blueprint)


@root_blueprint.route('/')
def index():
    """Rota principal do aplicativo."""
    return render_template('index.html')
