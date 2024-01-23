from flask import Blueprint
from flask_bcrypt import Bcrypt
from flask_restful import Api, Resource, reqparse, abort
from flask_jwt_extended import current_user, create_access_token, get_jwt_identity, jwt_required, JWTManager
from models import User

auth_bp = Blueprint('auth_bp', __name__)
bcrypt = Bcrypt()
jwt = JWTManager
api = Api(auth_bp)

signUp_args = reqparse.RequestParser()
signUp_args.add_argument('name',type=str,required=True, help='Last Name cannot be blank')
signUp_args.add_argument("email", type=str, required=True)
signUp_args.add_argument("password", type=str, required=True)
signUp_args.add_argument("confirmPassword", type=str, required=True)

login_args = reqparse.RequestParser()
login_args.add_argument("email", type=str, required=True)
login_args.add_argument("password", type=str, required=True)


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).first()


class Login(Resource):
    # def get(self):
    #     current_user_id = get_jwt_identity()
    #     user = User.query.get(current_user_id)
    #     if not user:
    #         return abort(404, detail="User is not found")
    #     return {"username": user.username, "user_id": user.id}

    def post(self):
        data = login_args.parse_args()
        user = User.query.filter_by(email=data['email']).first()

        if not user:
            return abort(404, detail="User does not exist")

        if not bcrypt.check_password_hash(user.password, data['password']):
            return abort(403, detail="Incorrect password")

        metadata = {"name": user.name}
        token = create_access_token(identity=user.id, additional_claims=metadata)
        return {"access_token": token}

api.add_resource(Login, "/login")