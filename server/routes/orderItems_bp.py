from flask import Blueprint, make_response, jsonify
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_restful import Api, Resource, abort, reqparse
from flask_marshmallow import Marshmallow

from models import OrderItem, db

orderItem_bp = Blueprint('orderItem_bp', __name__)
ma=Marshmallow(orderItem_bp)
api = Api(orderItem_bp)



post_args = reqparse.RequestParser()
post_args.add_argument('product_id', type=int, required=True, help='OrderItem product_id is required')
post_args.add_argument('user_id', type=int, required=True, help='OrderItem user_id is required')
post_args.add_argument('quantity', type=int, required=True, help='OrderItem quantity is required')
post_args.add_argument('price', type=float, required=True, help='OrderItem price is required')


patch_args = reqparse.RequestParser()
patch_args.add_argument('product_id', type=int)
patch_args.add_argument('user_id', type=int)
patch_args.add_argument('quantity', type=int)
patch_args.add_argument('price', type=float)



class OrderItemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = OrderItem
        include_fk=True

orderItemschema = OrderItemSchema()

class OrderItems(Resource):
    def get(self):
        orderItem = OrderItem.query.all()
        result = orderItemschema.dump(orderItem, many=True)
        response = make_response(jsonify(result), 200)

        return response

    def post(self):
        data = post_args.parse_args()

        # error handling
        # orderItem = OrderItem.query.filter_by(description=data.description).first()
        # if orderItem:
        #     abort(409, detail="Productname with the same description already exists")

        new_orderItme = OrderItem(product_id=data['product_id'], user_id=data['user_id'], quantity=data['quantity'], price=data['price'])
        db.session.add(new_orderItme)
        db.session.commit()

        result = orderItemschema.dump(new_orderItme)
        response = make_response(jsonify(result),201)

        return response

api.add_resource(OrderItems,'/orderItems')

class OrderItemById(Resource):
    def get(self, id):
        single_orderItem = OrderItem.query.filter_by(id=id).first()

        if not single_orderItem:
            abort(404, detail=f'OrderItem with {id} does not exist')

        else:
            result = orderItemschema.dump(single_orderItem)
            response = make_response(jsonify(result), 200)
            return response

    def patch(self, id):
        single_orderItem = OrderItem.query.filter_by(id=id).first()

        if not single_orderItem:
            abort(404, detail=f'OrderItem with {id} does not exist')

        data = patch_args.parse_args()
        for key, value in data.items():
            if value is None:
                continue
            setattr( single_orderItem, key, value)
        db.session.commit()
        result = orderItemschema.dump(single_orderItem)
        response = make_response(jsonify(result), 200)

        return response

        

    def delete(self, id):
        orderItem = OrderItem.query.filter_by(id=id).first()
        if not orderItem:
            abort(404, detail=f'OrderItem with id {id} does not exist')
        db.session.delete(orderItem)
        db.session.commit()

        response_body = {
            "message": "OrderItem successfully deleted"
        }

        response = make_response(response_body, 200)
        return response


api.add_resource(OrderItemById, '/orderItems/<int:id>')

