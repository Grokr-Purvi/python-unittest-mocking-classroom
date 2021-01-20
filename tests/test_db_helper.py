from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper
import time


class TestDBHelper(TestCase):

    def test_get_maximum_salary_without_mocking(self):
        start = time.time()
        db_helper = DbHelper()

        value = db_helper.get_maximum_salary()
        end = time.time()
        print('one without mocking ',(end-start))

    @patch('src.db_helper.DbHelper')
    def test_get_maximum_salary(self, Mock_DbHelper):
        db_helper = Mock_DbHelper()

        db_helper.get_maximum_salary.return_value = 500000
        start = time.time()
        actual= db_helper.get_maximum_salary()
        end= time.time()
        print('with mocking',(end-start))
        expected= 500000


        self.assertEqual(actual, expected)

    @patch('src.db_helper.DbHelper')
    def test_get_minimum_salary(self, Mock_DbHelper):
        db_helper = Mock_DbHelper()

        db_helper.get_minimum_salary.return_value = 500000

        actual= db_helper.get_minimum_salary()
        expected= 500000


        self.assertEqual(actual, expected)