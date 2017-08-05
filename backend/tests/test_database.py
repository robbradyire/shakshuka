# Testing file for database.py

import os
import unittest

from recipes import database
from recipes import environ

class TestRecipeDatabase(unittest.TestCase):

    def setUp(self):
        """Creates a test database if none exists"""
        test_rd = database.RecipeDatabase(test=True)
        test_rd.new_db()

    def tearDown(self):
        """Deletes the test database"""
        os.remove(os.environ["TEST_DB"])

    def test_create_recipe(self):
        test_rd = database.RecipeDatabase(test=True)
        test_rd.create_recipe({
            'name': "test recipe",
            'instructions': "One\nTwo\n",
            'link': "link.com",
            'comments': "tasty",
            'servings': "1-2"
        })
        q_result = test_rd.get_recipes()
        expected = [(1, "test recipe", "One\nTwo\n", "link.com", "tasty", "1-2")]
        self.assertListEqual(expected, q_result)

if __name__ == '__main__':
    unittest.main()

