# Sistema de Biblioteca Simples - API REST

Este projeto é uma API simples de gerenciamento de uma biblioteca, desenvolvida com Flask. Ela permite operações de CRUD (Create, Read, Update, Delete) para **clientes**, **livros** e **empréstimos**.

---

## Alunos

- **Vitor Boer** - 132695-2023
- **Guilherme Vieira** - 128409-2023
- **Natan Augusto** - 125651-2023
- **João Vítor Ferreira Duarte** - 130142-2023

**Data final (última alteração):** 21/04/2025  
**Data de entrega:** 22/04/2025

---

## Como executar

1. Instale o Flask (caso ainda não tenha):

   ```bash
   pip install flask
   ```

2. Execute o arquivo principal:

   ```bash
   python nome_do_arquivo.py
   ```

3. Acesse o endereço: `http://localhost:5000`

Você pode testar as rotas utilizando o Postman ou qualquer outra ferramenta de API REST, além de que, as requests estão comentadas no corpo do código.

---

## Rotas disponíveis (testes via Postman)

### CLIENTES

- `GET /clientes` - Listar todos os clientes
- `POST /clientes` - Cadastrar um novo cliente
- `PUT /clientes/{id}` - Atualizar um cliente pelo ID
- `DELETE /clientes/{id}` - Deletar um cliente pelo ID

### LIVROS

- `GET /livros` - Listar todos os livros
- `POST /livros` - Cadastrar um novo livro
- `PUT /livros/{id}` - Atualizar um livro pelo ID
- `DELETE /livros/{id}` - Deletar um livro pelo ID

### EMPRÉSTIMOS

- `GET /emprestimos` - Listar todos os empréstimos
- `POST /emprestimos` - Registrar um novo empréstimo
- `PUT /emprestimos/{id}` - Atualizar um empréstimo pelo ID
- `DELETE /emprestimos/{id}` - Deletar um empréstimo pelo ID

---

## 📂 Estrutura dos dados

### Exemplo de cliente

```json
{
  "nome": "João Silva",
  "email": "joao@example.com",
  "telefone": "1234-5678"
}
```

### Exemplo de livro

```json
{
  "titulo": "Python para Iniciantes",
  "autor": "Ricardo Costa",
  "ano": 2020,
  "status": "disponível"
}
```

### Exemplo de empréstimo

```json
{
  "livro_id": 1,
  "cliente_id": 2,
  "data_emprestimo": "2023-04-10",
  "data_devolucao": "2023-04-24",
  "status": "pendente"
}
```

---

## Tecnologias utilizadas

- Python 3.x
- Flask
- JSON (como simulação de banco de dados)
