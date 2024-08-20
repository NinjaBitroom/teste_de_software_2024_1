"""
Claudinei de Oliveira - pt-BR - 19-06-2023
Manipulando o banco de dados sqlite3 
Adaptado de Giridhar, 2016
"""
# Importando os módulos necessários do Flask
from flask import Blueprint, flash, redirect, render_template, request, url_for

from src.controllers.produto_controller import ProdutoController

produto_blueprint = Blueprint('produto', __name__, url_prefix='/produto')
"""Criando um Blueprint.

Este é um objeto que permite definir rotas em um módulo separado.
Um Blueprint, em Flask, é um jeito de organizar um grupo de rotas 
relacionadas, funções de visualização e outros recursos de código.
"""


@produto_blueprint.route('/')
def index():
    """Rota principal do aplicativo que exibe todos os produtos."""
    produtos = ProdutoController.get_produtos()
    """Obtém todos os produtos do banco de dados."""
    return render_template('produto/index.html', produtos=produtos)


@produto_blueprint.get('/novo')
def novo_produto_get():
    return render_template('produto/novo.html')


@produto_blueprint.post('/novo')
def novo_produto_post():
    """Rota para adicionar um novo produto."""
    fields = ('descricao', 'preco')
    produto = {}

    for field in fields:
        produto[field] = request.form.get(field)

    errors = ProdutoController.create_produto(
        descricao=produto['descricao'], preco=produto['preco']
    )

    if errors:
        for error in errors:
            flash(error)
        return redirect(url_for('root.produto.novo_produto_get'))

    return redirect(url_for('root.produto.index'))


@produto_blueprint.get('/editar/<int:id>')
def editar_produto_get(id: int):
    produto = ProdutoController.get_produto(id)
    return render_template('produto/editar.html', produto=produto)


@produto_blueprint.post('/editar/<int:id>')
def editar_produto_post(id: int):
    """Rota para atualizar um produto."""
    fields = ('descricao', 'preco', 'status')
    produto_dict = {}

    for field in fields:
        produto_dict[field] = request.form.get(field)

    produto = ProdutoController.update_produto(
        id, produto_dict['descricao'], produto_dict['preco'],
        produto_dict['status']
    )

    if isinstance(produto, ValueError):
        for msg in produto.args:
            flash(msg)
        return redirect(url_for('root.produto.editar_produto_get', id=id))

    return redirect(url_for('root.produto.index'))


@produto_blueprint.post('/deletar/<int:id>')
def deletar_produto(id: int):
    """Rota para deletar um produto."""
    ProdutoController.delete_produto(id)
    return redirect(url_for('root.produto.index'))
