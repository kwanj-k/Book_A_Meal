from flask_restful import reqparse, abort, Api, Resource

ORDERS = {
    'order1': {'item': 'Tea'},
    'order2': {'item': 'Ugali'},
    'order3': {'item': 'Fish'},
}




def abort_if_order_doesnt_exist(order_id):
    if order_id not in ORDERS:
        abort(404, message="Order {} doesn't exist".format(order_id))


parser = reqparse.RequestParser()
parser.add_argument('item')

#orders

class Order(Resource):
    def get(self, order_id):
        abort_if_order_doesnt_exist(order_id)
        return ORDERS[order_id]

    def delete(self, order_id):
        abort_if_order_doesnt_exist(order_id)
        del ORDERS[order_id]
        return '', 204

    def put(self, order_id):
        args = parser.parse_args()
        item = {'item': args['item']}
        ORDERS[order_id] = item
        return item, 201


class OrderList(Resource):
    def get(self):
        return ORDERS

    def post(self):
        args = parser.parse_args()
        order_id = int(max(ORDERS.keys()).lstrip('order')) + 1
        order_id = 'order%i' % order_id
        ORDERS[order_id] = {'item': args['item']}
        return ORDERS[order_id], 201