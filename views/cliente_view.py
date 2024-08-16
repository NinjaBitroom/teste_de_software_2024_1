"""
Claudinei de Oliveira - pt-BR - 19-06-2023
Manipulando o banco de dados sqlite3
Adaptado de Giridhar, 2016
"""
# Importando os módulos necessários do Flask
from flask import Blueprint, redirect, render_template, request, url_for, flash

from controllers.cliente_controller import ClienteController

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
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    logradouro = request.form.get('logradouro')
    numero = request.form.get('numero')
    complemento = request.form.get('complemento')
    bairro = request.form.get('bairro')
    cep = request.form.get('cep')
    cidade = request.form.get('cidade')
    uf = request.form.get('uf')
    telefone = request.form.get('telefone')
    email = request.form.get('email')
    ClienteController.create_cliente(
        nome, cpf, logradouro, numero, complemento,
        bairro, cep, cidade, uf, telefone, email
    )
    return redirect(url_for('root.cliente.index'))


@cliente_blueprint.get('/editar/<int:cpf>')
def editar_cliente_get(cpf: int):
    cliente = ClienteController.get_cliente(cpf)
    return render_template('cliente/editar.html', cliente=cliente)


@cliente_blueprint.post('/editar/<int:cpf>')
def editar_cliente_post(cpf: int):
    """Rota para atualizar um cliente."""

    descricao = request.form.get('descricao')
    """Obtém a descrição do cliente do form."""

    preco = request.form.get('preco')
    """Obtém o preço do cliente do form."""

    status = request.form.get('status')

    cliente = ClienteController.update_cliente(id, descricao, preco, status)

    if isinstance(cliente, ValueError):
        for msg in cliente.args:
            flash(msg)
        return redirect(url_for('root.cliente.editar_cliente_get', id=id))

    return redirect(url_for('root.cliente.index'))


@cliente_blueprint.route('/deletar/<int:cpf>', methods=['GET'])
def deletar_cliente(cpf: int):
    """Rota para deletar um cliente."""
    ClienteController.delete_cliente(cpf=cpf)
    return redirect(url_for('root.cliente.index'))
