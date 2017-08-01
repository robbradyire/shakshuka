# database.py
# contains the logic for interacting with the database

import os
import sqlite3

from . import environ

class RecipeDatabase:
    """Stores database interaction methods"""

    def __init__(self, test=True):
        """Creates a RecipeDatabase
        
        Params:
            test: chooses whether to use the test or production db
        returns: RecipeDatabase
        """
        if test:
            self.db = os.environ["TEST_DB"]
        else:
            self.db = os.environ["RECIPE_DB"]

    def new_db(self):
        """Creates a new database if there isn't one present already
        
        Params: None
        Returns: True or False
        """
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            with open('sql/create_tables.sql') as f:
                contents = f.read()
                cursor.executescript(contents)
            connection.commit()
            return True
        return False

    def drop_db(self):
        """Clear the database
        
        Params: None
        Return: True or False
        """
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            table_names = ["recipe","ingredient","recipe_ingredient",
                "tag", "recipe_tag"
            ] 
            for name in table_names:
                cursor.execute("DELETE FROM {}".format(name))
            connection.commit()
            return True
        return False

    ###################################
    # GET
    ###################################

    def get_recipes(self):
        """Return all recipe ids and names

        Params: None
        Return: list
        """
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id, name FROM recipe")
            return cursor.fetchall()
        return []

    def get_recipe(self, recipe_id):
        """Return a recipe by its ID
        
        Params:
            recipe_id: int
        Return: recipe OR None
        """
        with sqlite3.connect(self.db) as connection:
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

    def create_recipe(self, args):
        """Create a recipe
        
        Params:
            args: dict
        Return: True or None
        """
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            query = ' '.join((
                "INSERT INTO recipes",
                "(name, instructions, link, comments, servings)",
                "VALUES (?,?,?,?,?)",
            ))
            cursor.execute(query,
                (args["name"], args["instructions"], args["link"], 
                 args["comments"], args["servings"],))
            connection.commit()
            return True
        return None

    def create_recipe_ingredient(self, args):
        """Create a recipe ingredient
        
        Params:
            args: dict
        Return: True or None
        """
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            query = ' '.join((
                "INSERT INTO recipe_ingredient",
                "(recipe_id, ingredient_id, preparation, quantity)",
                "VALUES (?,?,?,?)",
            ))
            cursor.execute(query,
                (args["recipe_id"], args["ingredient_id"], args["preparation"], 
                 args["quantity"],))
            connection.commit()
            return True
        return None

    def create_recipe_tag(self, args):
        return None

    def create_ingredient(self, args):
        return None

    def create_tag(self, args):
        return None

    ###################################
    # UPDATE
    ###################################

    def update_recipe(self, recipe_id, args):
        return None

    def update_recipe_ingredient(self, recipe_id, ingredient_id, args):
        return None

    def update_recipe_tag(self, recipe_id, ingredient_id, args):
        return None

    def update_ingredient(self, recipe_id, args):
        return None

    def update_tag(self, recipe_id, tag_id, args):
        return None

    ###################################
    # DELETE
    ###################################

    def delete_recipe(self, recipe_id):
        """Delete a recipe by its ID

        Params:
            recipe_id: int
        Return: recipe or None
        """
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            cursor.execute("SQL")
            connection.commit()
            return cursor.fetchone()
        return None

    def delete_recipe_ingredient(self, recipe_id, ingredient_id, args):
        return None

    def delete_recipe_tag(self, recipe_id, ingredient_id, args):
        return None

    def delete_ingredient(self, recipe_id, args):
        return None

    def delete_tag(self, recipe_id, tag_id, args):
        return None

if __name__ == '__main__':
    print('2')

