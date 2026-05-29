#!/usr/bin/python3
"""Script to initialize the SQLite database with seed data."""
import sqlite3


def create_database():
    """Create Products table and insert sample data."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Create the table structure
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Insert initial data if it doesn't exist yet
    cursor.execute('''
        INSERT OR IGNORE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()

