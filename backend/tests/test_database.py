# Testing file for database.py

import os
import unittest

from recipes import database
from recipes import environ

class TestRecipeDatabase(unittest.TestCase):

    def test_init(self):
        test_rdb = database.RecipeDatabase()
        prod_rdb = database.RecipeDatabase(test=False)
        self.assertEqual(test_rdb.db, os.environ["TEST_DB"])
        self.assertEqual(prod_rdb.db, os.environ["RECIPE_DB"])

if __name__ == '__main__':
    unittest.main()

