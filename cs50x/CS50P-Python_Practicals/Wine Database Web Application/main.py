#!/usr/bin/python3

import sqlite3


# Function to create the wine database and tables
def create_database():
    conn = sqlite3.conncet('wine_database.db')
    c = conn.cursor()


