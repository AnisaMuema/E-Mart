from flask import Blueprint, make_response, jsonify
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_restful import Api, Resource, abort, reqparse
from flask_marshmallow import Marshmallow

from models import Category, db

category_bp = Blueprint('category_bp', __name__)
ma=Marshmallow(category_bp)
api = Api(category_bp)



post_args = reqparse.RequestParser()
post_args.add_argument('product_id', type=int, required=True, help='Category product_id is required')
post_args.add_argument('name', type=str, required=True, help='Category name is required')



patch_args = reqparse.RequestParser()
patch_args.add_argument('product_id', type=int)
patch_args.add_argument('name', type=int)




class CategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        include_fk=True

categoryschema = CategorySchema()

class Categories(Resource):
    def get(self):
        category = Category.query.all()
        result = categoryschema.dump(category, many=True)
        response = make_response(jsonify(result), 200)

        return response

    def post(self):
        data = post_args.parse_args()

        # error handling
        category = Category.query.filter_by(product_id=data.product_id, name=data.name).first()
        if category:
            abort(409, detail="Product already exists in category")

        new_category = Category(product_id=data['product_id'], name=data['name'])
        db.session.add(new_category)
        db.session.commit()

        result = categoryschema.dump(new_category)
        response = make_response(jsonify(result),201)

        return response

api.add_resource(Categories,'/categories')

class CategoryById(Resource):
    def get(self, id):
        single_category = Category.query.filter_by(id=id).first()

        if not single_category:
            abort(404, detail=f'Category with {id} does not exist')

        else:
            result = categoryschema.dump(single_category)
            response = make_response(jsonify(result), 200)
            return response

    def patch(self, id):
        single_category = Category.query.filter_by(id=id).first()

        if not single_category:
            abort(404, detail=f'Category with {id} does not exist')

        data = patch_args.parse_args()
        for key, value in data.items():
            if value is None:
                continue
            setattr( single_category, key, value)
        db.session.commit()
        result = categoryschema.dump(single_category)
        response = make_response(jsonify(result), 200)

        return response

        

    def delete(self, id):
        category = Category.query.filter_by(id=id).first()
        if not category:
            abort(404, detail=f'Category with id {id} does not exist')
        db.session.delete(category)
        db.session.commit()

        response_body = {
            "message": "Category successfully deleted"
        }

        response = make_response(response_body, 200)
        return response


api.add_resource(CategoryById, '/categories/<int:id>')