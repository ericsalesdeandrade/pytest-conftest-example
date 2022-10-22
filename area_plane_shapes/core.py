import logging
import math

# Set Logging
logging.basicConfig(level=logging.INFO)


class AreaPlaneShapes:
    def __init__(self, radius=None, base: int | float = None,
                 height: int | float = None, side: int | float = None):
        """
        Function to initialise the Area of Plane Shapes Class
        """
        # Validate `radius` of type int | float
        if isinstance(radius, int | float):
            self.radius = radius
        else:
            raise ValueError("Input `radius` should be of Type - Int or Float")

        # Validate `base` and `height` of type int | float
        if isinstance(base, int | float) and isinstance(height, int | float):
            self.base = base
            self.height = height
        else:
            raise ValueError("Inputs `base` and `height` should be of Type - Int or Float")

            # Validate `side` of type int | float
        if isinstance(side, int | float):
            self.side = side
        else:
            raise ValueError("Input `side` should be of Type - Int or Float")

    def area_of_triangle(self) -> int | float:
        """
        Function to calculate Area of Triangle
        Required Parameters - Base and Height, Type - int | float
       :return: Area, Type - int | float
        """
        try:
            area = 0.5 * self.base * self.height
            return area
        except Exception as err:
            logging.error(err)

    def area_of_circle(self) -> int | float:
        """
        Function to calculate Area of Circle
        Required Parameters - Radius, Type - int | float
        :return: Area, Type - int | float
        """
        try:
            area = math.pi * pow(self.radius, 2)
            return area
        except Exception as err:
            logging.error(err)

    def area_of_square(self) -> int | float:
        """
        Function to calculate Area of Square
        Required Parameters - Side, Type - int | float
       :return: Area, Type - int | float
        """
        try:
            area = pow(self.side, 2)
            return area
        except Exception as err:
            logging.error(err)

    def area_of_rectangle(self) -> int | float:
        """
        Function to calculate Area of Rectangle
        Required Parameters - Side and Height, Type - int | float
       :return: Area, Type - int | float
        """
        try:
            area = self.side * self.height
            return area
        except Exception as err:
            logging.error(err)

