import unittest
from models.rectangle import Rectangle

class TestRectangleMethods(unittest.TestCase):
    """Test cases for the Rectangle class methods."""

    def setUp(self):
        """Set up a Rectangle instance for testing."""
        self.rectangle = Rectangle(5, 10, 2, 3, 1)

    def test_init(self):
        """Test the initialization of the Rectangle instance."""
        self.assertEqual(self.rectangle.width, 5)
        self.assertEqual(self.rectangle.height, 10)
        self.assertEqual(self.rectangle.x, 2)
        self.assertEqual(self.rectangle.y, 3)
        self.assertEqual(self.rectangle.id, 1)

    def test_width_setter(self):
        """Test the setter method for the width attribute."""
        with self.assertRaises(TypeError):
            self.rectangle.width = "invalid"
        with self.assertRaises(ValueError):
            self.rectangle.width = -5
        self.rectangle.width = 7
        self.assertEqual(self.rectangle.width, 7)

    def test_height_setter(self):
        """Test the setter method for the height attribute."""
        with self.assertRaises(TypeError):
            self.rectangle.height = "invalid"
        with self.assertRaises(ValueError):
            self.rectangle.height = -10
        self.rectangle.height = 15
        self.assertEqual(self.rectangle.height, 15)

    def test_x_setter(self):
        """Test the setter method for the x attribute."""
        with self.assertRaises(TypeError):
            self.rectangle.x = "invalid"
        with self.assertRaises(ValueError):
            self.rectangle.x = -2
        self.rectangle.x = 4
        self.assertEqual(self.rectangle.x, 4)

    def test_y_setter(self):
        """Test the setter method for the y attribute."""
        with self.assertRaises(TypeError):
            self.rectangle.y = "invalid"
        with self.assertRaises(ValueError):
            self.rectangle.y = -3
        self.rectangle.y = 6
        self.assertEqual(self.rectangle.y, 6)

    def test_area(self):
        """Test the area method."""
        self.assertEqual(self.rectangle.area(), 5 * 10)

    def test_display(self):
        """Test the display method."""
        # TODO: Implement display method testing logic
        pass

    def test_update(self):
        """Test the update method."""
        self.rectangle.update(2, 8, 12, 5, 7)
        self.assertEqual(self.rectangle.id, 2)
        self.assertEqual(self.rectangle.width, 8)
        self.assertEqual(self.rectangle.height, 12)
        self.assertEqual(self.rectangle.x, 5)
        self.assertEqual(self.rectangle.y, 7)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        expected_dict = {
            'id': 1,
            'width': 5,
            'height': 10,
            'x': 2,
            'y': 3
        }
        self.assertEqual(self.rectangle.to_dictionary(), expected_dict)

    def test_str(self):
        """Test the str method."""
        expected_str = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(self.rectangle), expected_str)

if __name__ == '__main__':
    unittest.main()
