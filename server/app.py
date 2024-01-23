from flask import Flask
from flask_migrate import Migrate
from models import db
import os
from routes.users_bp import user_bp, bcrypt
from routes.product_bp import product_bp
from routes.profile_bp import profile_bp
from routes.reviews_bp import review_bp
from routes.orderItems_bp import orderItem_bp
from routes.categories_bp import category_bp
from routes.auth import auth_bp, jwt



def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///mart.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
    app.config['SECRET_KEY']= '39uhqfh34h340920i4hfd-2='
    # app.config['JWT_ACCESS_TOKEN_EXPIRES']=timedelta(hours=2)


    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(user_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(orderItem_bp)
    app.register_blueprint(category_bp)


    
    return app
