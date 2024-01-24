from flask_sqlalchemy import SQLAlchemy

db  = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    firstname=db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    orderItems = db.relationship('OrderItem', backref='user')
    profiles = db.relationship('Profile', backref='user')
    reviews = db.relationship('Review', backref='user')

    def __repr__(self):
        return f'<User {self.firstname} {self.lastname}>'
    
class Profile(db.Model):
    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id') )
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    location = db.Column(db.String)

    def __repr__(self):
        return f'<Profile {self.firstname}>'
    
class OrderItem(db.Model):
    __tablename__ = "orderItems"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    

    def __repr__(self):
        return f'<OrderItem {self.product_id, self.user_id, self.quantity}>'
    
class Product(db.Model):
    __tablename__ = "products"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    categories = db.relationship('Category', backref='product')
    reviews = db.relationship('Review', backref='product')

    def __repr__(self):
        return f'<Product {self.name}>'
    
class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    def __repr__(self):
        return f'<Category {self.name}>'
    
class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    rating = db.Column(db.Integer)
    content = db.Column(db.String)

    def __repr__(self):
        return f'<Review {self.user_id} {self.product_id} {self.rating} {self.content}>'
    

