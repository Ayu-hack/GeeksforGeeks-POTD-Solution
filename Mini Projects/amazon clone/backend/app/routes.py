import pyodbc
from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)

# Database connection setup


def get_db_connection(server='localhost\SQLEXPRESS', database='AmazonCloneDB'):
    try:

        connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

        connection = pyodbc.connect(connection_string)

        print(f"Connected to SQL Server: {server}, Database: {database}")

        return connection

    except pyodbc.Error as e:
        print(f"Error connecting to the database: {e}")
        return None


@main.route('/', methods=['GET'])
def home():
    return "Welcome to the Amazon Clone Backend API!"


@main.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('q')
    if not query:
        return jsonify([])

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        if query.isdigit():
            cursor.execute(
                "SELECT id, id, title, description, price FROM Products WHERE id = ? OR id = ?", (query, query))
        else:
            cursor.execute(
                "SELECT id, id, title, description, price FROM Products WHERE title LIKE ?", f'%{query}%')

        products = cursor.fetchall()

        products_json = [
            {"id": row[0], "id": row[1], "title": row[2],
                "description": row[3], "price": row[4]}
            for row in products
        ]

        conn.close()
        return jsonify(products_json)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@main.route('/products/<int:id>', methods=['GET'])
def get_product_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, id, title, description, price FROM Products WHERE id = ?", id)
    product = cursor.fetchone()

    conn.close()

    if product:
        product_json = {
            "id": product[0],
            "id": product[1],
            "title": product[2],
            "description": product[3],
            "price": product[4]
        }
        return jsonify(product_json)
    else:
        return jsonify({"error": "Product not found"}), 404
