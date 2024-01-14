import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_square_creation(self):
        """
        Test case for creating a Square instance.
        """
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertIsNone(square.id)

    def test_square_update(self):
        """
        Test case for updating the properties of a Square instance.
        """
        square = Square(5)
        square.update(1, 10, 20, 30)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 20)
        self.assertEqual(square.y, 30)

        square.update(size=15, x=25, y=35, id=2)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 15)
        self.assertEqual(square.x, 25)
        self.assertEqual(square.y, 35)

    def test_square_to_dictionary(self):
        """
        Test case for converting a Square instance to a dictionary.
        """
        square = Square(5, id=1, x=10, y=20)
        expected_dict = {"id": 1, "size": 5, "x": 10, "y": 20}
        self.assertEqual(square.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
