#!/usr/bin/python3
import csv
import turtle
import json

class Base:
    __nb_objects = 0
    
    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int): Optional. The identifier for the instance. If not provided,
                an identifier will be assigned based on the number of instances.
        """
        
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """

        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding='utf-8') as file:
            json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of dictionaries represented by json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: List of dictionaries represented by json_string.
        """

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes already set.

        Args:
            **dictionary: Double pointer to a dictionary.

        Returns:
            Base: Instance with all attributes set.
        """

        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances loaded from a file.

        Returns:
            list: List of instances.
        """

        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**d) for d in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize instances to CSV format and save to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """

        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize instances from a CSV file.

        Returns:
            list: List of instances.
        """

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instances.append(cls.create(id=int(row[0]), width=int(row[1]), height=int(row[2]),
                                                    x=int(row[3]), y=int(row[4])))
                    elif cls.__name__ == "Square":
                        instances.append(cls.create(id=int(row[0]), size=int(row[1]), x=int(row[2]), y=int(row[3])))
                return instances
        except FileNotFoundError:
            return []


    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Open a window and draw all the Rectangles and Squares using Turtle graphics.

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.
        """

        screen = turtle.Screen()
        screen.bgcolor("white")
        screen.title("Draw Rectangles and Squares")

        pen = turtle.Turtle()
        pen.speed(2)  # Set the drawing speed

        # Draw Rectangles
        for rectangle in list_rectangles:
            pen.penup()
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()
            pen.forward(rectangle.width)
            pen.left(90)
            pen.forward(rectangle.height)
            pen.left(90)
            pen.forward(rectangle.width)
            pen.left(90)
            pen.forward(rectangle.height)
            pen.left(90)

        # Draw Squares
        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)

        turtle.done()
