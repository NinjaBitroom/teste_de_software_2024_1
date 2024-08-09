"""
Claudinei de Oliveira - pt-BR - 19-06-2023
Manipulando o banco de dados sqlite3
Adaptado de Giridhar, 2016
"""
# Importando os módulos necessários do Flask
from flask import Blueprint, render_template, request, redirect, url_for, flash
# Importando a classe 'Cliente' do arquivo cliente_model.py
from models.cliente_model import Clientes

# Criando um Blueprint. Este é um objeto que permite definir rotas em um módulo separado.
# Um Blueprint, em Flask, é um jeito de organizar um grupo de rotas relacionadas, funções de visualização e outros
# recursos de código.
cliente_blueprint = Blueprint('cliente', __name__)


# Rota principal do aplicativo que exibe todos os clientes
@cliente_blueprint.route('/cliente/')
def index():
    clientes = Clientes.get_clientes()  # Obtém todos os clientes do banco de dados
    return render_template('cliente/novo.html', clientes=clientes)  # Renderiza o template novo.html com os clientes
