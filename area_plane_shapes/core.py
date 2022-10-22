import logging
import math

# Set Logging
logging.basicConfig(level=logging.INFO)


class AreaPlaneShapes:
    def __init__(self, radius=None, base: int | float = None,
                 height: int | float = None, side: int | float = None):
        """
        Function to initialise the Area of Plane Shapes Class
        https://www.mathsisfun.com/area.html
        """
        # Validate `radius` of type int | float
        if isinstance(radius, int | float | None):
            self.radius = radius
        else:
            raise ValueError("Input `radius` should be of Type - Int or Float")

        # Validate `base` and `height` of type int | float
        if isinstance(base, int | float | None) and isinstance(height, int | float | None):
            self.base = base
            self.height = height
        else:
            raise ValueError("Inputs `base` and `height` should be of Type - Int or Float")

            # Validate `side` of type int | float
        if isinstance(side, int | float | None):
            self.side = side
        else:
            raise ValueError("Input `side` should be of Type - Int or Float")

    def area_of_triangle(self) -> str:
        """
        Function to calculate Area of Triangle
        Required Parameters - Base and Height, Type - int | float
       :return: Area, Type - str
        """
        try:
            if all(item is not None for item in [self.base, self.height]):
                area = round(0.5 * self.base * self.height, 2)
                return f"The Area of the Triangle is `{area}` units"
            else:
                return "Area Unavailable. Please initialise Class with `Base` and `Height`"
        except Exception as err:
            logging.error(err)

    def area_of_circle(self) -> str:
        """
        Function to calculate Area of Circle
        Required Parameters - Radius, Type - int | float
        :return: Area, Type - str
        """
        try:
            if self.radius is not None:
                area = round(math.pi * pow(self.radius, 2), 2)
                return f"The Area of the Circle is `{area}` units"
            else:
                return "Area Unavailable. Please initialise Class with `Radius`"
        except Exception as err:
            logging.error(err)

    def area_of_square(self) -> str:
        """
        Function to calculate Area of Square
        Required Parameters - Side, Type - int | float
       :return: Area, Type - str
        """
        try:
            if self.side is not None:
                area = round(pow(self.side, 2), 2)
                return f"The Area of the Square is `{area}` units"
            else:
                return "Area Unavailable. Please initialise Class with `Side`"
        except Exception as err:
            logging.error(err)

    def area_of_rectangle(self) -> str:
        """
        Function to calculate Area of Rectangle
        Required Parameters - Side and Height, Type - int | float
       :return: Area, Type - str
        """
        try:
            if all(item is not None for item in [self.side, self.height]):
                area = round(self.side * self.height, 2)
                return f"The Area of the Rectangle is `{area}` units"
            else:
                return "Area Unavailable. Please initialise Class with `Side` and `Height`"
        except Exception as err:
            logging.error(err)

