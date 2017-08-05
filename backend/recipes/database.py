# database.py
# contains the logic for interacting with the database

import os
import sqlite3
import sys

from . import environ

class RecipeDatabase:
    """Stores database interaction methods"""

    def __init__(self, test=True):
        """Creates a RecipeDatabase
        
        :param test: Selects the test or the production DB
        :type test: Boolean
        :return: An object to interact with the database
        :rtype: RecipeDatabase
        """
        if test:
            self.db = os.environ["TEST_DB"]
        else:
            self.db = os.environ["RECIPE_DB"]

    def new_db(self):
        """Creates a new database if there isn't one present already
        
        :return: True or False
        :rtype: Boolean
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
        
        :return: True or False
        :rtype: Boolean
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
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id, name FROM recipe")
            return cursor.fetchall()
        return []

    def get_recipe(self, recipe_id):
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            query = ' '.join((
                "SELECT *",
                "FROM recipe WHERE id=?",
            ))
            cursor.execute(query, (recipe_id,))
            return cursor.fetchone()
        return None

    def get_ingredients(self):
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM ingredient")
            return cursor.fetchall()
        return []

    def get_tags(self):
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM tag")
            return cursor.fetchall()
        return []

    def get_recipe_ingredients(self, recipe_id):
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM recipe_ingredient")
            return cursor.fetchall()
        return []

    def get_recipe_tags(self, recipe_id):
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM recipe_tag")
            return cursor.fetchall()
        return []

    ###################################
    # CREATE
    ###################################

    def create_recipe(self, args):
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            query = ' '.join((
                "INSERT INTO recipe",
                "(name, instructions, link, comments, servings)",
                "VALUES (?,?,?,?,?)",
            ))
            cursor.execute(query,
                (args["name"], args["instructions"], args["link"], 
                 args["comments"], args["servings"],))
            connection.commit()
            return True
        return None

    def create_ingredient(self, args):
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO ingredient name VALUE ?"
            cursor.execute(query, args["name"])
            connection.commit()
            return True
        return None

    def create_tag(self, args):
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO tag name VALUE ?"
            cursor.execute(query, args["name"])
            connection.commit()
            return True
        return None

    def create_recipe_ingredient(self, args):
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
        with sqlite3.connect(self.db) as connection:
            cursor = connection.cursor()
            query = ' '.join((
                "INSERT INTO recipe_tag",
                "(recipe_id, tag_id)",
                "VALUES (?,?)",
            ))
            cursor.execute(query, (args["recipe_id"], args["tag_id"],))
            connection.commit()
            return True
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

