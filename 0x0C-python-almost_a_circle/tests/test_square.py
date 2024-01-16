import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_square_creation(self):
        square = Square(5, 10, 20, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 10)
        self.assertEqual(square.y, 20)
        self.assertEqual(square.id, 1)

    def test_square_to_dictionary(self):
        square = Square(5, 10, 20, 1)
        expected_dict = {'id': 1, 'width': 5, 'height': 5, 'x': 10, 'y': 20}
        self.assertEqual(square.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
