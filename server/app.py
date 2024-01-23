from flask import Flask
from flask_migrate import Migrate
from models import db
from routes.users_bp import user_bp



def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///mart.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(user_bp)


    
    return app
