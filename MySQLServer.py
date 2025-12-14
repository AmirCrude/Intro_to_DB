#!/usr/bin/env python3
"""
MySQLServer.py - Creates the alx_book_store database
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    """Create the alx_book_store database if it doesn't exist"""
    connection = None
    cursor = None
    
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Amir&mysql_1738"
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        
    finally:
        # Close the connection
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()