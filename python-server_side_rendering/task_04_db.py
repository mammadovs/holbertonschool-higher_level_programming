#!/usr/bin/python3
"""Flask application serving HTML templates using Jinja and SQLite."""
import csv
import json
import sqlite3
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


def read_sql(product_id=None):
    """Read and parse data from SQLite database products.db."""
    products = []
    try:
        conn = sqlite3.connect('products.db')
        # Use sqlite3.Row to access columns by their actual names
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        if product_id:
            cursor.execute(
                "SELECT id, name, category, price FROM Products WHERE id = ?",
                (product_id,)
            )
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")

        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": row["id"],
                "name": row["name"],
                "category": row["category"],
                "price": row["price"]
            })
        conn.close()
    except sqlite3.Error:
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
    """Render products from JSON, CSV, or SQL based on query parameters."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Validation 1: Check if source is valid
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # Load data based on the specified source
    if source == 'json':
        data = read_json()
        if product_id is not None:
            try:
                target_id = int(product_id)
                data = [p for p in data if p.get('id') == target_id]
            except ValueError:
                data = []

    elif source == 'csv':
        data = read_csv()
        if product_id is not None:
            try:
                target_id = int(product_id)
                data = [p for p in data if p.get('id') == target_id]
            except ValueError:
                data = []

    else:  # source == 'sql'
        if product_id is not None:
            try:
                target_id = int(product_id)
                data = read_sql(target_id)
            except ValueError:
                return render_template(
                    'product_display.html',
                    error="Product not found"
                )
        else:
            data = read_sql()

    # Validation 2: Check if product was not found when an ID was provided
    if product_id is not None and not data:
        return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

