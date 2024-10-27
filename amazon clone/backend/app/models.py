from . import db

from .extensions import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)


    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': str(self.price)
        }

def get_all_products():
    return [product.to_dict() for product in Product.query.all()]

def get_product_by_id(product_id):
    product = Product.query.get(product_id)
    return product.to_dict() if product else None

def add_product(product_data):
    new_product = Product(
        title=product_data['title'],
        description=product_data['description'],
        price=product_data['price']
    )
    db.session.add(new_product)
    db.session.commit()

def update_product(product_id, updates):
    product = Product.query.get(product_id)
    if product:
        product.title = updates.get('title', product.title)
        product.description = updates.get('description', product.description)
        product.price = updates.get('price', product.price)
        db.session.commit()
        return product.to_dict()
    return None
