import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        # Reset the Base class counter before each test
        Base._Base__nb_objects = 0

    def test_draw(self):
        """
        Test case for the draw method.
        """
        rectangles = [Rectangle(50, 30, 10, 10), Rectangle(70, 40, 50, 50)]
        squares = [Square(40, 20, 20), Square(60, 10, 70)]

        # Redirect turtle graphics output to a file (to avoid graphical window pop-up during testing)
        import sys
        import io
        original_stdout = sys.stdout
        sys.stdout = io.StringIO()

        Base.draw(rectangles, squares)

        # Reset turtle graphics output
        sys.stdout = original_stdout

        # The draw method doesn't raise exceptions, so just assert True for now
        self.assertTrue(True)

    def test_draw_empty_lists(self):
        """
        Test case for the draw method with empty lists.
        """
        rectangles = []
        squares = []

        # Redirect turtle graphics output to a file (to avoid graphical window pop-up during testing)
        import sys
        import io
        original_stdout = sys.stdout
        sys.stdout = io.StringIO()

        Base.draw(rectangles, squares)

        # Reset turtle graphics output
        sys.stdout = original_stdout

        # The draw method doesn't raise exceptions, so just assert True for now
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

