#!/usr/bin/python3

import sqlite3


# Function to create the wine database and tables
def create_database():
    conn = sqlite3.conncet("wine_database.db")
    c = conn.cursor()

    # Create teh wines table
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

    # Create the sales tables
    c.execute(
        """CREATE TABLE IF NOT EXISTS sales
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
               wine_id INTEGER NOT NULL,
               outlet_id INTEGER NOT NULL,
               quantity INTEGER NOT NULL,
               FOREIGN_KEY(wine_id) REFERENCES wines(id),
               FOREIGN_KEY(outlet_id) REFERENCES outlets(id))"""
    )

    conn.commit()
    conn.close()


# Function to add a wine to the database
def add_wine(name, capacity):
    conn = sqlite3.connect("wine_database.db")
    c = conn.cursor()
    c.execute("INSERT INTO wines (name, capacity) VALUES(?, ?)", (name, capacity))
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
        "INSERT INTO sales(wine_id, outlet_id, quantity) VALUES(?, ?, ?)",
        (wine_id, outlet_id, quantity),
    )
    c.excute("UPDATE outlets SET stock = stock - ? WHERE id = ?", (quantity, outlet_id))
    conn.commit()
    conn.close()


# Function to display the wine database
def display_database():
    conn = sqlite3.connect("wine_database.db")
    c = conn.cursor()

    # Display wines
    c.execute("SELECT * FROM wines")
    print("Wines:")
    print("{:<5} {:<15} {:<10}".format("ID", "Name", "Capacity"))
    for row in c.fetchall():
        print("{:<5} {:<15} {:<10}".format(row[0], row[1], row[2]))

    # Display outlets
    c.execute("SELECT * FROM outlets")
    print("\nOutlets:")
    print("{:<5} {:<15} {:<10}".format("ID", "Name", "Stock"))
    for row in c.fetchall():
        print("{:<5} {:<15} {:<10}".format(row[0], row[1], row[2]))

    # Display sales
    c.execute(
        """SELECT sales.id, wines.name, outlets.name, sales.quantity
              FROM sales
              INNER JOIN wines ON sales.wine_id = wines.id
              INNER JOIN outlets ON sales.outlet_id = outlets.id"""
    )
    print("\nSales:")
    print("{:<5} {:<15} {:<15} {:<10}".format("ID", "Wine", "Outlet", "Quantity"))
    for row in c.fetchall():
        print("{:<5} {:<15} {:<15} {:<10}".format(row[0], row[1], row[2], row[3]))

    conn.close()


# Example
