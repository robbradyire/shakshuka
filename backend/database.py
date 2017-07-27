# database.py
# contains the logic for interacting with the database

import sqlite3

###################################
# GET
###################################

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

def get_recipe(recipe_id):
    """Return a recipe by its ID
    
    Params:
        recipe_id: int
    Return: recipe OR None
    """
    with sqlite3.connect("recipes.db") as connection:
        cursor = connection.cursor()
        query = ' '.join((
            "SELECT *",
            "FROM recipes WHERE id=?",
        ))
        cursor.execute(query, (recipe_id,))
        return cursor.fetchone()
    return None

###################################
# CREATE
###################################

def create_recipe(args):
    """Create a recipe
    
    Params:
        args: dict
    Return: True or None
    """
    with sqlite3.connect("recipes.db") as connection:
        cursor = connection.cursor()
        query = ' '.join((
            "INSERT INTO recipes",
            "(name, instructions, link, comments, servings)",
            "VALUES (?,?,?,?,?)",
        ))
        cursor.execute(query,
            (args["name"], args["instructions"], args["link"], 
             args["comments"], args["servings"],))
        cursor.commit()
        return True
    return None

def create_recipe_ingredient(args):
    """Create a recipe ingredient
    
    Params:
        args: dict
    Return: True or None
    """
    with sqlite3.connect("recipes.db") as connection:
        cursor = connection.cursor()
        query = ' '.join((
            "INSERT INTO recipe_ingredient",
            "(recipe_id, ingredient_id, preparation, quantity)",
            "VALUES (?,?,?,?)",
        ))
        cursor.execute(query,
            (args["recipe_id"], args["ingredient_id"], args["preparation"], 
             args["quantity"],))
        cursor.commit()
        return True
    return None

def create_recipe_tag(args):
    return None

def create_ingredient(args):
    return None

def create_tag(args):
    return None

###################################
# UPDATE
###################################

def update_recipe(recipe_id, args):
    return None

def update_recipe_ingredient(recipe_id, ingredient_id, args):
    return None

def update_recipe_tag(recipe_id, ingredient_id, args):
    return None

def update_ingredient(recipe_id, args):
    return None

def update_tag(recipe_id, tag_id, args):
    return None

###################################
# DELETE
###################################

def delete_recipe(recipe_id):
    """Delete a recipe by its ID

    Params:
        recipe_id: int
    Return: recipe or None
    """
    with sqlite3.connect("recipes.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SQL")
        cursor.commit()
        return cursor.fetchone()
    return None

def delete_recipe_ingredient(recipe_id, ingredient_id, args):
    return None

def delete_recipe_tag(recipe_id, ingredient_id, args):
    return None

def delete_ingredient(recipe_id, args):
    return None

def delete_tag(recipe_id, tag_id, args):
    return None

