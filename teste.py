# Nomes...........: Vitor Boer, Guilherme Vieira- 128409-2023, Natan Augusto- 125651-2023
# Data final......: 21/04/2025
# data de entrega.: 22/04/2025
# Objetivo........: Criar um controle de estoque simples com Flask em python usando um banco simulado.

from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulando um banco de dados com dados referentes a um controle de estoque simples
tarefas = [
    {"id": 1, "teste1": "Estudar Python", "descricao": "Revisar listas", "status": "pendente"},
    {"id": 2, "titulo": "Fazer exercício", "descricao": "Criar uma API com Flask", "status": "em andamento"}
]

# GET /tarefas
@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)

# POST /tarefas
@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    nova_tarefa = request.get_json()
    nova_tarefa['id'] = len(tarefas) + 1
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

# DELETE /tarefas/<id>
@app.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefas.remove(tarefa)
            return jsonify({"mensagem": "Tarefa removida com sucesso"}), 200
    return jsonify({"erro": "Tarefa não encontrada"}), 404

@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    for tarefa in tarefas:
        if tarefa['id'] == id:
            nova_tarefa = request.get_json()
            tarefa.update(nova_tarefa)
            return jsonify(tarefa), 200
    return jsonify({"erro": "Tarefa não encontrada"}), 404

# Inicia a aplicação
if __name__ == '__main__':
    app.run(debug=True)
