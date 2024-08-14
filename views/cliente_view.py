"""
Claudinei de Oliveira - pt-BR - 19-06-2023
Manipulando o banco de dados sqlite3
Adaptado de Giridhar, 2016
"""
# Importando os módulos necessários do Flask
from flask import Blueprint, render_template

from controllers.cliente_controller import ClienteController

# Importando a classe 'Cliente' do arquivo cliente_model.py

cliente_blueprint = Blueprint('cliente', __name__, url_prefix='/cliente')
""" Criando um Blueprint.

Este é um objeto que permite definir rotas em um módulo separado.
Um Blueprint, em Flask, é um jeito de organizar um grupo de rotas
relacionadas, funções de visualização e outros recursos de código.
"""


@cliente_blueprint.route('/')
def index():
    """Rota principal do aplicativo que exibe todos os clientes."""

    clientes = ClienteController.get_clientes()
    """Obtém todos os clientes do banco de dados."""

    return render_template(
        'cliente/index.html', clientes=clientes
    )


@cliente_blueprint.route('/novo')
def novo_cliente():
    """Rota para adicionar um novo cliente."""

    return render_template('cliente/novo.html')
