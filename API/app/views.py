from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from app import app


meals = {
    0: 'BreakFast',
    1: 'Brunch',
    2: 'Lunch',
    3: 'Dinner',
    4: 'Supper',
}

def meal_repr(key):
    return {
        'url': request.host_url.rstrip('/') + url_for('meals_detail', key=key),
        'name': meals[key]
    }


@app.route("/", methods=['GET', 'POST'])
def meals_list():
    """
    List or create meals.
    """
    if request.method == 'POST':
        meal = str(request.data.get('name', ''))
        idx = max(meals.keys()) + 1
        meals[idx] = meal
        return meal_repr(idx), status.HTTP_201_CREATED

    # request.method == 'GET'
    return [meal_repr(idx) for idx in sorted(meals.keys())]


@app.route("/<int:key>/", methods=['GET', 'PUT', 'DELETE'])
def meals_detail(key):
    """
    Retrieve, update or delete meal instances.
    """
    if request.method == 'PUT':
        meal = str(request.data.get('name', ''))
        meals[key] = meals
        return meal_repr(key)

    elif request.method == 'DELETE':
        meals.pop(key, None)
        return '', status.HTTP_204_NO_CONTENT

    # request.method == 'GET'
    if key not in meals:
        raise exceptions.NotFound()
    return meal_repr(key)
