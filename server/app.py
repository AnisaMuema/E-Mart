from flask import Flask
from flask_migrate import Migrate
from models import db
from routes.users_bp import user_bp
from routes.product_bp import product_bp
from routes.profile_bp import profile_bp
from routes.reviews_bp import review_bp
from routes.orderItems_bp import orderItem_bp
from routes.categories_bp import category_bp


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///mart.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(user_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(orderItem_bp)
    app.register_blueprint(category_bp)


    
    return app
