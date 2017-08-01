# Testing file for database.py

import os
import unittest

# import path environment
from . import project_paths

from recipes import RecipeDatabase
from recipes import environ

class TestRecipeDatabase(unittest.TestCase):

    def test_init(self):
        test_rdb = RecipeDatabase()
        prod_rdb = RecipeDatabase(test=False)
        self.assertEqual(test_rdb.db, os.environ["TEST_DB"])
        self.assertEqual(prod_rdb.db, os.environ["RECIPE_DB"])

if __name__ == '__main__':
    unittest.main()

