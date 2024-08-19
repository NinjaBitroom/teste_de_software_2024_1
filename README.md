# Teste de Software - 2024

## Grupo

- Everton (Discente)
- Gabriel (Discente)
- Wanderson (Discente)
- Claudinei (Docente)

## Descrição

Atividade de Teste de Software do dia 08/08/2024.

## Tarefas

- [x] Baixar o código da aula 08/08/2024
- [x] Baixar o código da aula 11/04/2024 (na aula de 18/04/2024)
- [x] Integrar ambos os códigos
- [x] Adicionar validação de e-mail no model dos clientes
- [x] Adicionar validação de telefone no model dos clientes
- [ ] Adicionar testes de unidade para os models dos clientes
- [ ] Adicionar testes de unidade para os models dos produtos
- [ ] Adicionar testes de integração para os models dos clientes
- [ ] Adicionar testes de integração para os models dos produtos

## Requisitos

- Python 3.12

## Como rodar

### Preparação do ambiente

```powershell
python -m venv venv
. .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Execução do servidor

```powershell
flask run
```

### Execução dos testes

```powershell
python -m tests.test_cliente
python -m tests.test_produto_model
```
