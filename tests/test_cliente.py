"""
Claudinei de Oliveira - utf-8 - pt-br
testeModel.py
"""

from src.models.cliente_model import ClienteModel

# testando a classe Cliente
while True:
    print('Digite as informações do cliente:')
    nome = input('Nome: ')
    cpf = input('CPF (11 dígitos): ')
    logradouro = input('Logradouro: ')
    numero = input('Número: ')
    complemento = input('Complemento (opcional): ')
    bairro = input('Bairro: ')
    cep = input('CEP (formato 00000-000): ')
    cidade = input('Cidade: ')
    uf = input('UF (duas letras maiúsculas): ')
    telefone = input('Telefone: ')
    email = input('Email: ')
    try:
        cliente = ClienteModel(
            nome=nome, cpf=cpf, telefone=telefone, email=email,
            logradouro=logradouro, numero=numero,
            complemento=complemento, bairro=bairro, cep=cep,
            cidade=cidade, uf=uf,
        )

        print('\nCliente criado com sucesso!')
        endereco_formatado = f"{cliente.endereco['logradouro']}, {cliente.endereco['numero']} - {cliente.endereco['complemento']}, {cliente.endereco['bairro']} - {cliente.endereco['cep']}, {cliente.endereco['cidade']}/{cliente.endereco['uf']}"
        print(
            f'Nome: {cliente.nome}, CPF: {cliente.cpf}, Endereço: {endereco_formatado}, '
            f'Telefone: {cliente.telefone}, Email: {cliente.email}'
        )
        # Se o cliente foi criado com sucesso, quebra o loop (se desejado)
        break  # Remova esta linha se desejar que o loop continue indefinidamente
    except ValueError as e:
        print(f'\nErro ao criar o cliente: {e}\nPor favor, tente novamente.')
        # Não use 'break' aqui para continuar o loop
