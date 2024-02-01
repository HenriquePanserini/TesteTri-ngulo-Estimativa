from model import ResultTriangle

def calculation_sum_max(triangle):

    result_calculation = [line.copy() for line in triangle]

    for i in range(len(result_calculation[i])):
        for j in range(len(result_calculation[i])):

            result_calculation[i][j] += max(result_calculation[i + 1][j], result_calculation[i + 1][j + 1])
    
    return result_calculation[0][0]

    def save_result_mongodb(triangle, result_calculation, db):
        result_id = db.results.insert_one({
            'triangle' : triangle,
            'result: ' : result_calculation
        }).inserted_id
        return result_id
    
    def calculation_sum_max_and_save(triangle, db):
        result_calculation = calculation_sum_max(triangle)
        result_id = save_result_mongodb(triangle, result_calculation, db)
        return ResultTriangle(triangle, result_calculation, result_id)
    

        