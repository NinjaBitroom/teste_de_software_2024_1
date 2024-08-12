"""
Claudinei de Oliveira - pt-BR - 19-06-2023
Manipulando o banco de dados sqlite3 
Adaptado de Giridhar, 2016
"""
# Importando os módulos necessários do Flask
from flask import Blueprint, flash, redirect, render_template, request, url_for

# Importando a classe 'Produto' do arquivo produto_model.py
from models.produto_model import Produto

produto_blueprint = Blueprint('produto', __name__)
"""Criando um Blueprint.

Este é um objeto que permite definir rotas em um módulo separado.
Um Blueprint, em Flask, é um jeito de organizar um grupo de rotas 
relacionadas, funções de visualização e outros recursos de código.
"""


@produto_blueprint.route('/produto/')
def index():
    """Rota principal do aplicativo que exibe todos os produtos."""
    produtos = Produto.get_produtos()
    """Obtém todos os produtos do banco de dados."""
    return render_template(
        'produto/novo.html', produtos=produtos
    )  # Renderiza o template novo.html com os produtos


@produto_blueprint.route('/produto/novo', methods=['GET', 'POST'])
def novo_produto():
    """Rota para adicionar um novo produto."""
    if request.method == 'POST':  # Se o método da requisição é POST
        descricao = request.form.get('descricao')
        """Obtém a descrição do produto do form."""

        preco = request.form.get('preco')
        """Obtém o preço do produto do form."""

        # Verifica se o preço é um número válido
        try:
            preco = float(preco)
        except ValueError:
            flash(
                'O preço deve ser um número válido.'
            )  # Exibe uma mensagem de erro
            produtos = Produto.get_produtos()
            """Obtém todos os produtos do banco de dados."""
            return render_template(
                'produto/novo.html',
                produtos=produtos
            )  # Renderiza o template novo.html com os produtos

        produto = Produto(
            descricao=descricao, preco=preco
        )
        """Cria uma nova instância do produto."""
        produto.salvar()  # Salva o produto no banco de dados

    produtos = Produto.get_produtos()
    """Obtém todos os produtos do banco de dados."""

    return render_template(
        'produto/novo.html', produtos=produtos
    )  # Renderiza o template novo.html com os produtos


@produto_blueprint.route('/produto/editar/<float:id>', methods=['GET', 'POST'])
def editar_produto(id):
    """Rota para atualizar um produto."""
    produto = Produto.get_produto(id)
    """Obtém o produto pelo ID."""

    if request.method == 'POST':  # Se o método da requisição é POST
        descricao = request.form.get('descricao')
        """Obtém a descrição do produto do form."""

        preco = request.form.get('preco')
        """Obtém o preço do produto do form."""

        # Verifica se o preço é um número válido
        try:
            preco = float(preco)
        except ValueError:
            flash(
                'O preço deve ser um número válido.'
            )  # Exibe uma mensagem de erro
            return render_template(
                'produto/atualizar.html',
                produto=produto
            )  # Renderiza o template editar.html com o produto

        produto.descricao = descricao  # Atualiza a descrição do produto
        produto.preco = preco  # Atualiza o preço do produto
        produto.atualizar()  # Atualiza o produto no banco de dados
        return redirect(
            url_for('produto.index')
        )  # Redireciona para a rota '/'
    return render_template(
        'produto/atualizar.html', produto=produto
    )  # Renderiza o template editar.html com o produto


@produto_blueprint.route(
    '/produto/atualizar/<int:id>/<int:status>', methods=['GET', 'POST']
)  # 'status' adicionado como parâmetro
def atualizar_produto(
    id, status
):  # Alteração aqui, 'status' adicionado como parâmetro
    """Rota para atualizar o status de um produto."""
    produto = Produto.get_produto(id)
    """Obtém o produto pelo ID."""
    produto.status = status  # Atualiza o status do produto
    produto.atualizar()  # Atualiza o produto no banco de dados
    return redirect(url_for('produto.index'))  # Redireciona para a rota '/'


@produto_blueprint.route('/produto/deletar/<id>', methods=['GET'])
def deletar_produto(id):
    """Rota para deletar um produto."""
    produto = Produto.get_produto(id)
    """Obtém o produto pelo ID."""
    produto.deletar()  # Deleta o produto do banco de dados
    return redirect(url_for('produto.index'))  # Redireciona para a rota '/'
