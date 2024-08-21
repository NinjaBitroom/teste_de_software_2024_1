"""
Claudinei de Oliveira - pt-BR - 19-06-2023
Manipulando o banco de dados sqlite3
Adaptado de Giridhar, 2016
"""
# Importando os módulos necessários do Flask
from flask import Blueprint, flash, redirect, render_template, request, url_for

from src.controllers.cliente_controller import ClienteController

cliente_blueprint = Blueprint('cliente', __name__, url_prefix='/cliente')
"""Criando um Blueprint.

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


@cliente_blueprint.get('/novo')
def novo_cliente_get():
    """Rota para adicionar um novo cliente."""
    clientes = ClienteController.get_clientes()
    return render_template('cliente/novo.html', clientes=clientes)


@cliente_blueprint.post('/novo')
def novo_cliente_post():
    """Rota para adicionar um novo cliente."""
    fields = (
        'nome', 'cpf', 'logradouro', 'numero', 'complemento', 'bairro', 'cep',
        'cidade', 'uf', 'telefone', 'email'
    )
    cliente_dict = {field: request.form.get(field) for field in fields}
    error = ClienteController.create_cliente(cliente_dict)
    if error is not None:
        for msg in error.args:
            flash(msg)
        return redirect(url_for('root.cliente.novo_cliente_get'))
    return redirect(url_for('root.cliente.index'))


@cliente_blueprint.get('/editar/<int:id>')
def editar_cliente_get(id: int):
    cliente = ClienteController.get_cliente(id)
    return render_template('cliente/editar.html', cliente=cliente)


@cliente_blueprint.post('/editar/<int:id>')
def editar_cliente_post(id: int):
    """Rota para atualizar um cliente."""
    fields = (
        'nome', 'cpf', 'logradouro', 'numero', 'complemento', 'bairro', 'cep',
        'cidade', 'uf', 'telefone', 'email'
    )
    cliente_dict: dict[str, str | None | int] = {
        field: request.form.get(field) for field in fields
    }
    cliente_dict['id'] = id
    cliente = ClienteController.update_cliente(**cliente_dict)
    if isinstance(cliente, ValueError):
        for msg in cliente.args:
            flash(msg)
        return redirect(url_for('root.cliente.editar_cliente_get', id=id))
    return redirect(url_for('root.cliente.index'))


@cliente_blueprint.post('/deletar/<int:id>')
def deletar_cliente(id: int):
    """Rota para deletar um cliente."""
    ClienteController.delete_cliente(id)
    return redirect(url_for('root.cliente.index'))
