<strong> Projeto - Triangulo de estimativa maxima</strong>

1.Resumo: <br><br>
    Aplicação que recebe uma serie de numeros, nesses que se encontram numa estrutura triangular, onde o calculo desses valores nessa estrutura são calculados de cima para baixo entre os numeros proximos um do outro

2.Adição de diretorio model: <br><br>
    Adição de arquivo model para parametrização de variaveis que serão necessarias para contrução e calculo do triangulo de estimativa nessa model são compostos por;<br><br>
    
        self.triangle = triangle
        self.result = result
    
Valores que tambem serão atribuidos a banco não-relacional para sua persistencia.

3.Adição de metodo service: <br><br>
    Adição de metodo de service_calculation para execução do calculo do triangulo de estimativa.

    def calculation_sum_max(triangle):

    result_calculation = [line.copy() for line in triangle]

    for i in range(len(result_calculation[i])):
        for j in range(len(result_calculation[i])):

            result_calculation[i][j] += max(result_calculation[i + 1][j], result_calculation[i + 1][j + 1])
    
    return result_calculation[0][0]

  Alem disso nessa service tambem foi adicionado uma função para realizar o salvamento dos dados obetidos no banco de dados MongoDB.<br><br>

        def save_result_mongodb(triangle, result_calculation, db):
  
        result_id = db.results.insert_one({
            'triangle' : triangle,
            'result: ' : result_calculation
        }).inserted_id
        
        return result_id

E uma ultima função criada para que ambas funções de calculo e de salvamento em banco de dados possam ser executadas.<br><br>

         def calculation_sum_max_and_save(triangle, db):
 
        result_calculation = calculation_sum_max(triangle)
        
        result_id = save_result_mongodb(triangle, result_calculation, db)
        
        return ResultTriangle(triangle, result_calculation, result_id)

4.Adição de arquivo root app.py: <br><br>
    Arquivo de execução principal foi nomeado de app.py é nele em que esta sendo feito a conexão ao banco de dados nao-relacional e a definição das rotas da aplicação.
    Nele tambem se encontra um metodo para executar as funções do arquivo service_calculation para que o calculo seja feito e os dados salvos nas collections.

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
    
