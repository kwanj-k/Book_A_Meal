from flask import Flask,request,jsonify,make_response
from flask_restful import reqparse, abort, Api, Resource
from resources.meal import Meal,MealList
from resources.menu import Menu,MenuList
from resources.order import Order,OrderList


app = Flask(__name__)
api = Api(app)

@app.route('/api/v1/login')
def login():
    data = request.get_json()

    
    return make_response(jsonify({
                                 "status": "ok",
                                 "message": "You are logged in" 
                                 }), 200)

@app.route('/api/v1/register',  methods = ['POST'])
def register():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']

    # for user in users:
    #     if username == user.username:
    #         if email == user.email
    #         return jsonify({'status':202 , 
    #             'message':'User already exists. Please login.'}), 202
    
    # new_user = User(username, phone, password, email=email)
    # users.append(new_user)

    return make_response(jsonify({
                                 "status": "ok",
                                 "username": username , 
                                 "email": email, 
                                 "password": password
                                 }), 201)






api.add_resource(MealList, '/api/v1/meals')
api.add_resource(Meal, '/api/v1/meals/<meal_id>')

api.add_resource(MenuList, '/api/v1/menus')
api.add_resource(Menu, '/api/v1/menus/<menu_id>')

api.add_resource(OrderList, '/api/v1/orders')
api.add_resource(Order, '/api/v1/orders/<order_id>')


if __name__ == '__main__':
    app.run(debug=True)