import unittest
from application import application


class FlaskAppTest(unittest.TestCase):
    def setUp(self):
        self.app = application.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        data = response.data.decode('utf-8')
        self.assertIn('Hello world! BigData z Pythonem!', data)

if __name__ == '__main__':
    unittest.main()
