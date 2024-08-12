"""
Claudinei de Oliveira - pt-BR - 19-06-2023
Adaptado de Giridhar, 2016
O arquivo main.py arquivo principal 
"""

# Importação das bibliotecas e módulos necessários
from flask import render_template

from setup import create_app, create_tables

app = create_app()
"""Cria a instância do aplicativo Flask e configura o banco de dados."""

create_tables(app)  # Cria as tabelas no banco de dados se necessário


@app.route('/')
def index():
    """Rota principal do aplicativo."""
    return render_template('index.html')
