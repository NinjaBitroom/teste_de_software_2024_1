"""
Claudinei de Oliveira - pt-BR, UTF-8 - 15-08-2024
Manipulando o banco de dados sqlite3 
Test_Integ_ProdModel_produtoCont
"""

def test_integration_novo_to_index(self):
    # Testa a criação de um novo produto e verifica se ele aparece na index
    self.client.post('/novo', data={'descricao': 'Produto Integrado', 'preco': 20.0})
    response = self.client.get('/')
    self.assertIn(b'Produto Integrado', response.data)

def test_integration_deleta_to_index(self):
    # Testa a deleção de um produto e verifica se ele foi removido da index
    produto = Produto(descricao='Produto para Deletar', preco=30.0)
    db.session.add(produto)
    db.session.commit()
    self.client.get(f'/deleta/{produto.id}')
    response = self.client.get('/')
    self.assertNotIn(b'Produto para Deletar', response.data)


