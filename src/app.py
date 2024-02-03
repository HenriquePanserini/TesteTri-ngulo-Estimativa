from flask import Flask, request, jsonify
from pymongo import MongoClient
from model.model_calculation import ResultTriangle
from service.service_calculation import calculation_sum_max, calculation_sum_max_and_save

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017')
db = client['TesteTrianguloDB']

@app.route('/', methods=['GET'])
def home():
    return 'Bem-vindo ao Teste do Triângulo!'

@app.route('/triangulo', methods=['POST'])
def calculation_sum_max_handler():
    data = request.get_json()
    triangle = data.get('triangulo')

    result_obj = calculation_sum_max_and_save(triangle, db)

    return jsonify({'result_id': str(result_obj.result_id)})

if __name__ == '__main__':
    app.run(debug=True)