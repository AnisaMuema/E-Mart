from flask import Blueprint, make_response, jsonify
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_restful import Api, Resource, abort, reqparse
from flask_marshmallow import Marshmallow
from flask_jwt_extended import jwt_required

from models import Product, db

product_bp = Blueprint('product_bp', __name__)
ma=Marshmallow(product_bp)
api = Api(product_bp)



post_args = reqparse.RequestParser()
post_args.add_argument('name', type=str, required=True, help='Product name is required')
post_args.add_argument('description', type=str, required=True, help='Product description is required')
post_args.add_argument('quantity', type=int, required=True, help='Product quantity is required')
post_args.add_argument('price', type=float, required=True, help='Product product is required')


patch_args = reqparse.RequestParser()
patch_args.add_argument('name', type=str)
patch_args.add_argument('description', type=str)
patch_args.add_argument('quantity', type=int)
patch_args.add_argument('price', type=float)



class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product

productschema = ProductSchema()

class Products(Resource):
    def get(self):
        products = Product.query.all()
        result = productschema.dump(products, many=True)
        response = make_response(jsonify(result), 200)

        return response
    
    @jwt_required
    def post(self):
        data = post_args.parse_args()

        # error handling
        product = Product.query.filter_by(description=data.description).first()
        if product:
            abort(409, detail="Productname with the same description already exists")

        new_product = Product(name=data['name'], description=data['description'], quantity=data['quantity'], price=data['price'])
        db.session.add(new_product)
        db.session.commit()

        result = productschema.dump(new_product)
        response = make_response(jsonify(result),201)

        return response

api.add_resource(Products,'/products')

class ProductById(Resource):
    def get(self, id):
        single_product = Product.query.filter_by(id=id).first()

        if not single_product:
            abort(404, detail=f'Product with {id} does not exist')

        else:
            result = productschema.dump(single_product)
            response = make_response(jsonify(result), 200)
            return response

    @jwt_required
    def patch(self, id):
        single_product = Product.query.filter_by(id=id).first()

        if not single_product:
            abort(404, detail=f'Product with {id} does not exist')

        data = patch_args.parse_args()
        for key, value in data.items():
            if value is None:
                continue
            setattr( single_product, key, value)
        db.session.commit()
        result = productschema.dump(single_product)
        response = make_response(jsonify(result), 200)

        return response

        
    @jwt_required
    def delete(self, id):
        product = Product.query.filter_by(id=id).first()
        if not product:
            abort(404, detail=f'Product with id {id} does not exist')
        db.session.delete(product)
        db.session.commit()

        response_body = {
            "message": "Product successfully deleted"
        }

        response = make_response(response_body, 200)
        return response


api.add_resource(ProductById, '/products/<int:id>')


