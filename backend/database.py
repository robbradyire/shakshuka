# database.py
# contains the logic for interacting with the database

import sqlite3

def get_recipes():
    """Return all recipe ids and names

    Params: None
    Return: list
    """
    with sqlite3.connect("recipes.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, name FROM recipe")
        return cursor.fetchall()
    return []

def get_recipe(id):
    """Return a recipe by its ID
    
    Params:
        id: int
    Return: recipe OR None
    """
    with sqlite3.connect("recipes.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, instructions, link, comments, servings FROM recipes WHERE id=?", (id,))
        return cursor.fetchone()
    return None

