from typing import Any

import phonenumbers
import regex


class ClienteValidator:
    @staticmethod
    def valida_nome(nome: str) -> str:
        if not nome:
            raise ValueError('Nome inválido.')
        pattern = r'^[\p{L}\'\-\s]+$'
        if not regex.match(pattern, nome):
            raise ValueError(
                'Nome inválido. Não use números ou caracteres especiais.'
            )
        nome = regex.sub(r'\s+', ' ', nome).strip()
        partes_do_nome = nome.split()
        preposicoes = ['da', 'de', 'do', 'das', 'dos']
        nome_formatado = ' '.join(
            [
                parte.capitalize() if parte.lower() not in preposicoes else parte.lower()
                for parte in partes_do_nome]
        )
        return nome_formatado

    @staticmethod
    def valida_cpf(cpf: str) -> str:
        # verifica se o CPF possui exatamente 11 dígitos e se todos são
        # numéricos
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError('CPF inválido. Deve ter 11 dígitos numéricos...')

        # elimina CPFs invalidos conhecidos
        if cpf in ['0' * 11, '1' * 11, '2' * 11, '3' * 11, '4' * 11, '5' * 11,
            '6' * 11, '7' * 11, '8' * 11, '9' * 11]:
            raise ValueError('CPF inválido. Sequência repetida...')

        # Validação dos dígitos verificadores
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        resto = soma % 11
        if resto < 2:
            digito1 = 0
        else:
            digito1 = 11 - resto

        if int(cpf[9]) != digito1:
            raise ValueError(
                'CPF inválido. Dígito verificador 1 não confere...'
            )

        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        resto = soma % 11
        if resto < 2:
            digito2 = 0
        else:
            digito2 = 11 - resto

        if int(cpf[10]) != digito2:
            raise ValueError(
                'CPF inválido. Dígito verificador 2 não confere...'
            )

        return cpf  # retorna True se o CPF for válido

    @staticmethod
    def valida_email(email: str) -> Any:
        """
        valida o email, garantindo que contenha um @
        """
        if '@' not in email:
            raise ValueError('Email inválido.')
        return email

    @staticmethod
    def formata_texto(texto: str) -> str:
        # Capitaliza cada palavra corretamente, exceto preposições
        return ' '.join(
            word.capitalize() if word.lower() not in ['da', 'de', 'do', 'das',
                'dos'] else word.lower() for word in
                regex.sub(r'\s+', ' ', texto).strip().split()
        )

    @staticmethod
    def valida_endereco(
        logradouro: str, numero: Any, complemento: Any, bairro: str, cep: str,
        cidade: str, uf: str
    ):
        # Aplica a formatação correta de texto
        logradouro = ClienteValidator.formata_texto(logradouro)
        bairro = ClienteValidator.formata_texto(bairro)
        cidade = ClienteValidator.formata_texto(cidade)

        # Verifica se os campos obrigatórios estão preenchidos
        if not all([logradouro, numero, bairro, cep, cidade, uf]):
            raise ValueError(
                'Todos os campos de endereço, exceto complemento, são obrigatórios.'
            )

        # Validação do CEP com formato específico (00000-000)
        if not regex.match(r'^\d{5}-\d{3}$', cep):
            raise ValueError('CEP inválido. Deve seguir o formato 00000-000.')

        # Validação do UF para garantir que sejam duas letras maiúsculas
        if not regex.match(r'^[A-Z]{2}$', uf):
            raise ValueError(
                'UF inválido. Deve ser composto por duas letras maiúsculas.'
            )

        return logradouro, numero, complemento, bairro, cep, cidade, uf

    @classmethod
    def valida_telefone(cls, telefone: str) -> str:
        if not phonenumbers.is_possible_number_string(telefone, 'BR'):
            raise ValueError('Telefone inválido.')
        return telefone
