<strong> Projeto - Triangulo de estimativa maxima</strong>

1.Resumo: <br><br>
    Aplicação que recebe uma serie de numeros, nesses que se encontram numa estrutura triangular, onde o calculo desses valores nessa estrutura são calculados de cima para baixo entre os numeros proximos um do outro

2.Adição de diretorio model: <br><br>
    Adição de arquivo model para parametrização de variaveis que serão necessarias para contrução e calculo do triangulo de estimativa nessa model são compostos por;<br><br>
    
        self.triangle = triangle
        self.result = result
    
Valores que tambem serão atribuidos a banco não-relacional para sua persistencia

3.Adição de metodo service: <br><br>
    Adição de metodo de service_calculation para execução do calculo do triangulo de estimativa.

    def calculation_sum_max(triangle):

    result_calculation = [line.copy() for line in triangle]

    for i in range(len(result_calculation[i])):
        for j in range(len(result_calculation[i])):

            result_calculation[i][j] += max(result_calculation[i + 1][j], result_calculation[i + 1][j + 1])
    
    return result_calculation[0][0]
