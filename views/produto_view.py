"""
Claudinei de Oliveira - pt-BR - 19-06-2023
Manipulando o banco de dados sqlite3 
Adaptado de Giridhar, 2016
"""
# Importando os módulos necessários do Flask
from flask import Blueprint, flash, redirect, render_template, request, url_for

from controllers.produto_controller import ProdutoController
# Importando a classe 'Produto' do arquivo produto_model.py
from models.produto_model import Produto

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


@produto_blueprint.post('/novo')
def novo_produto():
    """Rota para adicionar um novo produto."""

    descricao = request.form.get('descricao')
    """Obtém a descrição do produto do form."""

    preco = request.form.get('preco')
    """Obtém o preço do produto do form."""

    errors = ProdutoController.create_produto(
        descricao=descricao, preco=preco
    )
    """Cria uma nova instância do produto."""

    for error in errors:
        flash(error)

    return redirect(url_for('root.produto.index'))


@produto_blueprint.get('/editar/<int:id>')
def editar_produto_get(id):
    produto = ProdutoController.get_produto(id)
    return render_template('produto/atualizar.html', produto=produto)


@produto_blueprint.post('/editar/<int:id>')
def editar_produto_post(id):
    """Rota para atualizar um produto."""

    descricao = request.form.get('descricao')
    """Obtém a descrição do produto do form."""

    preco = request.form.get('preco')
    """Obtém o preço do produto do form."""

    produto = ProdutoController.update_produto(id, descricao, preco)

    if isinstance(produto, ValueError):
        for msg in produto.args:
            flash(msg)
        return redirect(url_for('root.produto.editar_produto_get', id=id))

    return redirect(url_for('root.produto.index'))


@produto_blueprint.route(
    '/atualizar/<int:id>/<int:status>', methods=['GET', 'POST']
)  # 'status' adicionado como parâmetro
def atualizar_produto(
    id, status
):  # Alteração aqui, 'status' adicionado como parâmetro
    """Rota para atualizar o status de um produto."""
    produto = Produto.get_produto(id)
    """Obtém o produto pelo ID."""
    produto.status = status  # Atualiza o status do produto
    produto.atualizar()  # Atualiza o produto no banco de dados
    return redirect(
        url_for('root.produto.index')
    )  # Redireciona para a rota '/'


@produto_blueprint.route('/deletar/<id>', methods=['GET'])
def deletar_produto(id):
    """Rota para deletar um produto."""
    produto = Produto.get_produto(id)
    """Obtém o produto pelo ID."""
    produto.deletar()  # Deleta o produto do banco de dados
    return redirect(
        url_for('root.produto.index')
    )  # Redireciona para a rota '/'
