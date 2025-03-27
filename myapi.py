#url base - localhost
# endpoints
# - localhost/carros (GET)
# - localhost/carros (POST)
# - localhost/carros/id (GET)
# - localhost/carros/id (PUT)
# - localhost/carros (DELETE)

from flask import Flask, jsonify, request

app = Flask(__name__)

carros = [
    {
        'id':1,
        'nome':"Fox",
        'marca':"Volkswagem",
        'ano':"2014"
    },
    {
        'id':2,
        'nome':"Cruze",
        'marca':"Chevrolet",
        'ano':"2018"
    },
    {
        'id':3,
        'nome':"Taos",
        'marca':"Volkswagem",
        'ano':"2023"
    },
]
@app.route('/carros', methods=["GET"])
def obter_carro():
    return jsonify(carros)


@app.route('/carros/<int:id>', methods=["GET"])
def obter_id(id):
    for carro in carros:
        if carro.get('id') == id:
            return jsonify(carro)

@app.route('/carros/<int:id>', methods=["PUT"])
def editar_carro(id):
    carro_alterado = request.get_json()
    for indice,carro in enumerate(carros):
        if carro.get('id') == id:
            carros[indice].update(carro_alterado)
            return jsonify(carros[indice])

@app.route('/carros', methods=["POST"])
def incluir_carro():
    new_car = request.get_json()
    carros.append(new_car)

    return jsonify(carros)


@app.route('/carros/<int:id>', methods=["DELETE"])
def excluir_carro(id):
    for indice, carro in enumerate(carros):
        if carro.get('id') == id:
            del carros[indice]
    return jsonify(carros)

app.run(port=5000,host='localhost',debug=True)