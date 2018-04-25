from flask import Flask, jsonify

app = Flask(__name__)

# meals = [
#     {
#         'id': 1,
#         'meal_name': 'Lunch',
#         'description': 'Milk, Cheese, Pizza, Fruit, Tylenol', 
#         'done': False
#     },
#     {
#         'id': 2,
#         'meal_name': 'Lunch',
#         'menu': 'Milk, Cheese, Pizza, Fruit, Tylenol', 
#         'done': False
#     }
# ]

# @app.route('/api/v1/meals', methods=['GET'])
# def get_meals():
#     return jsonify({'meals': meals})

if __name__ == '__main__':
    app.run(debug=True)