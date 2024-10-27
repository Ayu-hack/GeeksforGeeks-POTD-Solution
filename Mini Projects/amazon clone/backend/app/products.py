# app/products.py

from typing import List, Dict

products = [
    {"id": 1, "title": "Sample Product 1", "description": "Description for product 1", "price": 29.99},
    {"id": 2, "title": "Sample Product 2", "description": "Description for product 2", "price": 39.99},
]

def get_all_products() -> List[Dict]:
    return products

def get_product_by_id(product_id: int) -> Dict:
    return next((product for product in products if product["id"] == product_id), None)
