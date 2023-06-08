from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


# Function to create the wine database and tables
def create_database():
    conn = sqlite3.connect("wine_database.db")
    c = conn.cursor()

    # Create the wines table
    c.execute(
        """CREATE TABLE IF NOT EXISTS wines
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                capacity INTEGER NOT NULL)"""
    )

    # Create the outlets table
    c.execute(
        """CREATE TABLE IF NOT EXISTS outlets
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                stock INTEGER NOT NULL)"""
    )

    # Create the sales table
    c.execute(
        """CREATE TABLE IF NOT EXISTS sales
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                wine_id INTEGER NOT NULL,
                outlet_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                FOREIGN KEY (wine_id) REFERENCES wines (id),
                FOREIGN KEY (outlet_id) REFERENCES outlets (id))"""
    )

    conn.commit()
    conn.close()


# Function to add a wine to the database
def add_wine(name, capacity):
    conn = sqlite3.connect("wine_database.db")
    c = conn.cursor()
    c.execute("INSERT INTO wines (name, capicity) VALUES (?, ?)", (name, capacity))
    conn.commit()
    conn.close()


# Function to add an outlet to the database
def add_outlet(name, stock):
    conn = sqlite3.connect("wine_database.db")
    c = conn.cursor()
    c.execute("INSERT INTO outlets (name, stock) VALUES (?, ?)", (name, stock))
    conn.commit()
    conn.close()


# Function to record a wine sale
def record_sale(wine_id, outlet_id, quantity):
    conn = sqlite3.connect("wine_database.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO sales (wine_id, outlet_id, quantity) VALUES (?, ?, ?)",
        (wine_id, outlet_id, quantity),
    )
    c.execute(
        "UPDATE outlets SET stock = stock - ? WHERE id = ?", (quantity, outlet_id)
    )
    conn.commit()
    conn.close()


# Function to fetch the wine data
def get_wines():
    conn = sqlite3.connect("wine_database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM wines")
    wines = c.fetchall()
    conn.close()
    return wines


# Function to fetch the outlet data
def get_outlets():
    conn = sqlite3.connect("wine_database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM outlets")
    outlets = c.fetchall()
    conn.close()
    return outlets


# Function to fetch sales data
def get_sales():
    conn = sqlite3.connect("wine_database.db")
    c = conn.cursor()
    c.execute(
        """SELECT sales.id, wines.name, outlets.name, sales.quantity
                FROM sales
                INNER JOIN wines ON sales.wine_id = wines.id
                INNER JOIN outlest ON sales.outlet_id = outlets.id"""
    )
    sales = c.fetchall()
    conn.close()
    return sales


# Route to display the home page
@app.route('/')
def home():
    return render_template('index.html')
# def home():
#     wines = get_wines()
#     outlets = get_outlets()
#     sales = get_sales()
#     return render_template("index.html", wines=wines, outlets=outlets, sales=sales)


# Route to handle form submission for adding a wine
@app.route('/add_wine', methods=['POST'])
def add_wine_route():
    name = request.form['wine_name']
    capacity = request.form['wine_capacity']
    add_wine(name, capacity)
    return home()


# Route to handle form submission for adding an outlet
@app.route('/add_outlet', methods=['POST'])
def add_outlet_route():
    name = request.form['outlet_name']
    stock = request.form['outlet_stock']
    add_outlet(name, stock)
    return home()


# Route to handle form submission for recording a sale
@app.route('/record_sale', methods=['POST'])
def record_sale_route():
    wine_id = request.form['wine_id']
    outlet_id = request.form['outlet_id']
    quantity = request.form['sale_quantity']
    record_sale(wine_id, outlet_id, quantity)
    return home()


if __name__ == '__main__':
    # create_database()
    app.run()