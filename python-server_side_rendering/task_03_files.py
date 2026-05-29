#!/usr/bin/python3
"""Flask application serving HTML templates using Jinja."""
import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    """Read and parse data from products.json."""
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv():
    """Read and parse data from products.csv."""
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except (FileNotFoundError, ValueError, KeyError):
        pass
    return products


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render the items page with data loaded from a JSON file."""
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get("items", [])
    except FileNotFoundError:
        items_list = []

    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    """Render products from JSON or CSV based on query parameters."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Validation 1: Check if source is valid
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # Load data from the specified source
    if source == 'json':
        data = read_json()
    else:
        data = read_csv()

    # Validation 2: Filter by ID if it is provided
    if product_id is not None:
        try:
            target_id = int(product_id)
            filtered_data = [p for p in data if p.get('id') == target_id]

            if not filtered_data:
                return render_template(
                    'product_display.html',
                    error="Product not found"
                )
            data = filtered_data
        except ValueError:
            return render_template(
                'product_display.html',
                error="Product not found"
            )

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

