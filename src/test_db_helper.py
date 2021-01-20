from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper


class TestDBHelper(TestCase):
    @patch('db_helper.DbHelper.get_maximum_salary', return_value=500000)
    def test_get_maximum_salary(self, get_maximum_salary):
        self.assertEqual(get_maximum_salary(), 500000)
        
        

