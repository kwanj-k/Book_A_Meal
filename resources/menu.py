from flask_restful import reqparse, abort, Api, Resource

MENUS = {}




def abort_if_menu_doesnt_exist(menu_id):
    if menu_id not in MENUS:
        abort(404, message="Menu {} doesn't exist".format(menu_id))


parser = reqparse.RequestParser()
parser.add_argument('name')

#Menus

class Menu(Resource):
    def get(self, menu_id):
        abort_if_menu_doesnt_exist(menu_id)
        return MENUS[menu_id]

    def delete(self, menu_id):
        abort_if_meal_doesnt_exist(menu_id)
        del MENUS[menu_id]
        return '', 204

    def put(self, menu_id):
        args = parser.parse_args()
        name = {'name': args['name']}
        MENUS[menu_id] = name
        return name, 201


class MenuList(Resource):
    def get(self):
        return MENUS

    def post(self):
        args = parser.parse_args()
        menu_id = int(max(MENUS.keys()).lstrip('menu')) + 1
        menu_id = 'menu%i' % menu_id
        MENUS[menu_id] = {'name': args['name']}
        return MENUS[menu_id], 201