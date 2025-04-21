# Nomes...........: Vitor Boer - 132695-2023, Guilherme Vieira - 128409-2023, Natan Augusto - 125651-2023, João Vítor Ferreira Duarte - 130142-2023
# Data final......: 21/04/2025
# Data de entrega.: 22/04/2025
# Objetivo........: Criar um sistema de biblioteca simples onde seja possível fazer empréstimos de livros. Atividade feita apenas para
#                   fins didáticos, não se deve considerar a lógica do programa.

# -----------------------------------------------
# API - Sistema de Biblioteca (Testes via Postman)
# -----------------------------------------------
# ---------- CLIENTES ----------

# GET - Listar todos os clientes
# GET http://localhost:5000/clientes

# POST - Cadastrar um novo cliente
# POST http://localhost:5000/clientes

# PUT - Atualizar um cliente existente
# PUT http://localhost:5000/clientes/1 (atualizar por id)

# DELETE - Deletar um cliente pelo ID 
# DELETE http://localhost:5000/clientes/1 (deletar por id)

# ---------- LIVROS ----------

# GET - Listar todos os livros
# GET http://localhost:5000/livros

# POST - Cadastrar um novo livro
# POST http://localhost:5000/livros

# PUT - Atualizar um livro existente (atualizar por id)
# PUT http://localhost:5000/livros/1

# DELETE - Deletar um livro pelo ID 
# DELETE http://localhost:5000/livros/1 (deletar por id)

# ---------- EMPRÉSTIMOS ----------

# GET - Listar todos os empréstimos
# GET http://localhost:5000/emprestimos

# POST - Registrar um novo empréstimo
# POST http://localhost:5000/emprestimos

# PUT - Atualizar um empréstimo existente 
# PUT http://localhost:5000/emprestimos/1 (atualizar por id)

# DELETE - Deletar um empréstimo pelo ID 
# DELETE http://localhost:5000/emprestimos/1 (deletar por id)

from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulando banco de dados, dados fictícios
clientes = [
    {"id": 1, "nome": "João Silva", "email": "joao@example.com", "telefone": "1234-5678"},
    {"id": 2, "nome": "Maria Oliveira", "email": "maria@example.com", "telefone": "9876-5432"},
    {"id": 3, "nome": "Carlos Souza", "email": "carlos@example.com", "telefone": "1122-3344"},
    {"id": 4, "nome": "Fernanda Pereira", "email": "fernanda@example.com", "telefone": "5566-7788"}
]

livros = [
    {"id": 1, "titulo": "Python para Iniciantes", "autor": "Ricardo Costa", "ano": 2020, "status": "disponível"},
    {"id": 2, "titulo": "Flask e Desenvolvimento Web", "autor": "Mariana Rocha", "ano": 2021, "status": "emprestado"},
    {"id": 3, "titulo": "Inteligência Artificial", "autor": "Luiz Almeida", "ano": 2019, "status": "disponível"},
    {"id": 4, "titulo": "Estruturas de Dados e Algoritmos", "autor": "Juliana Martins", "ano": 2018, "status": "disponível"}
]

emprestimos = [
    {"id": 1, "livro_id": 2, "cliente_id": 1, "data_emprestimo": "2023-04-10", "data_devolucao": "2023-04-24", "status": "pendente"},
    {"id": 2, "livro_id": 4, "cliente_id": 3, "data_emprestimo": "2023-04-12", "data_devolucao": "2023-04-26", "status": "pendente"},
    {"id": 3, "livro_id": 1, "cliente_id": 2, "data_emprestimo": "2023-04-15", "data_devolucao": "2023-04-29", "status": "pendente"},
    {"id": 4, "livro_id": 3, "cliente_id": 4, "data_emprestimo": "2023-04-17", "data_devolucao": "2023-05-01", "status": "pendente"}
]

# CLIENTES

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    return jsonify(clientes)

@app.route('/clientes', methods=['POST'])
def cadastrar_cliente():
    novo = request.get_json()
    novo['id'] = len(clientes) + 1
    clientes.append(novo)
    return jsonify(novo), 201

@app.route('/clientes/<int:id>', methods=['PUT'])
def atualizar_cliente(id):
    for cliente in clientes:
        if cliente['id'] == id:
            dados = request.get_json()
            cliente.update(dados)
            return jsonify(cliente), 200
    return jsonify({"erro": "Cliente não encontrado"}), 404

@app.route('/clientes/<int:id>', methods=['DELETE'])
def deletar_cliente(id):
    for cliente in clientes:
        if cliente['id'] == id:
            clientes.remove(cliente)
            return jsonify({"mensagem": "Cliente removido"}), 200
    return jsonify({"erro": "Cliente não encontrado"}), 404

# LIVROS

@app.route('/livros', methods=['GET'])
def listar_livros():
    return jsonify(livros)

@app.route('/livros', methods=['POST'])
def cadastrar_livro():
    novo = request.get_json()
    novo['id'] = len(livros) + 1
    livros.append(novo)
    return jsonify(novo), 201

@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    for livro in livros:
        if livro['id'] == id:
            dados = request.get_json()
            livro.update(dados)
            return jsonify(livro), 200
    return jsonify({"erro": "Livro não encontrado"}), 404

@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    for livro in livros:
        if livro['id'] == id:
            livros.remove(livro)
            return jsonify({"mensagem": "Livro removido"}), 200
    return jsonify({"erro": "Livro não encontrado"}), 404

# EMPRÉSTIMOS

@app.route('/emprestimos', methods=['GET'])
def listar_emprestimos():
    return jsonify(emprestimos)

@app.route('/emprestimos', methods=['POST'])
def registrar_emprestimo():
    novo = request.get_json()
    novo['id'] = len(emprestimos) + 1
    emprestimos.append(novo)
    return jsonify(novo), 201

@app.route('/emprestimos/<int:id>', methods=['PUT'])
def atualizar_emprestimo(id):
    for emprestimo in emprestimos:
        if emprestimo['id'] == id:
            dados = request.get_json()
            emprestimo.update(dados)
            return jsonify(emprestimo), 200
    return jsonify({"erro": "Empréstimo não encontrado"}), 404

@app.route('/emprestimos/<int:id>', methods=['DELETE'])
def deletar_emprestimo(id):
    for emprestimo in emprestimos:
        if emprestimo['id'] == id:
            emprestimos.remove(emprestimo)
            return jsonify({"mensagem": "Empréstimo removido"}), 200
    return jsonify({"erro": "Empréstimo não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
