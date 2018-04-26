from flask_restful import reqparse, abort, Api, Resource

MEALS = {
    'meal1': {'name': 'Breakfast'},
    'meal2': {'name': 'Lunch'},
    'meal3': {'name': 'Supper'},
}

def abort_if_meal_doesnt_exist(meal_id):
    if meal_id not in MEALS:
        abort(404, message="Meal {} doesn't exist".format(meal_id))

parser = reqparse.RequestParser()
parser.add_argument('name')

class Meal(Resource):
    def get(self, meal_id):
        abort_if_meal_doesnt_exist(meal_id)
        return MEALS[meal_id]

    def delete(self, meal_id):
        abort_if_meal_doesnt_exist(meal_id)
        del MEALS[meal_id]
        return '', 204

    def put(self, meal_id):
        args = parser.parse_args()
        name = {'name': args['name']}
        MEALS[meal_id] = name
        return name, 201


class MealList(Resource):
    def get(self):
        return MEALS

    def post(self):
        args = parser.parse_args()
        meal_id = int(max(MEALS.keys()).lstrip('meal')) + 1
        meal_id = 'meal%i' % meal_id
        MEALS[meal_id] = {'name': args['name']}
        return MEALS[meal_id], 201