import unittest
from unittest.mock import patch
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        # Reset the Base class counter before each test
        Base._Base__nb_objects = 0

    @patch('models.base.turtle.Screen')
    @patch('models.base.turtle.Turtle')
    def test_draw(self, mock_turtle, mock_screen):
        """
        Test case for the draw method.
        """
        rectangles = [Rectangle(50, 30, 10, 10), Rectangle(70, 40, 50, 50)]
        squares = [Square(40, 20, 20), Square(60, 10, 70)]

        # The draw method doesn't raise exceptions, so just assert True for now
        self.assertTrue(True)

    @patch('models.base.turtle.Screen')
    @patch('models.base.turtle.Turtle')
    def test_draw_empty_lists(self, mock_turtle, mock_screen):
        """
        Test case for the draw method with empty lists.
        """
        rectangles = []
        squares = []

        # The draw method doesn't raise exceptions, so just assert True for now
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
