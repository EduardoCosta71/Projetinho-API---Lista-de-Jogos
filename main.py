from flask import Flask, jsonify, request

app = Flask(__name__)

jogos = [
    {
        'id': 1,
        'nome': 'Residente Evil Remake',
        'plataforma': 'Console',
        'categoria': 'Terror',
        'multiplayer': False
    },
    {
        'id': 2,
        'nome': 'Valorant',
        'plataforma': 'PC',
        'categoria': 'FPS',
        'multiplayer': True
    },
    {
        'id': 3,
        'nome': 'Rainbow Six Siege',
        'plataforma': 'PC',
        'categoria': 'FPS',
        'multiplayer': True
    }
]

@app.route('/jogos', methods=['GET'])
def ver_jogos():
    return jsonify(jogos)

@app.route('/jogos/<int:id>', methods=['GET'])
def ver_jogos_id(id):
    for jogo in jogos:
        if jogo.get('id') == id:
            return jsonify(jogo)
    return jsonify({'erro': 'jogo não encontrado'}),404

@app.route('/jogos/<int:id>', methods=['PUT'])
def editar_jogos(id):
    jogo_alterar = request.get_json()
    for indice,jogo in enumerate(jogos):
        if jogo.get('id') == id:
            jogos[indice].update(jogo_alterar)
            return jsonify(jogos[indice])
        
@app.route('/jogos', methods=["POST"])
def jogo_novo():
    jogo_novo = request.get_json()
    jogos.append(jogo_novo)
    return jsonify(jogos)

@app.route('/jogos/<int:id>', methods=['DELETE'])
def excluir_id(id):
    for indice,excluir in enumerate(jogos):
        if excluir.get('id') == id:
            del jogos[indice]
            return jsonify(jogos)

app.run(port=5000,host='localhost',debug=True)
