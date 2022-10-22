import pytest
from area_plane_shapes.core import AreaPlaneShapes


@pytest.fixture(scope="class")
def area_fixture():
    area_plane_shapes_obj = AreaPlaneShapes(radius=2,
                                            base=2,
                                            height=4,
                                            side=3)
    return area_plane_shapes_obj


def test_area_of_triangle(area_fixture) -> None:
    """
    Unit Test for Area of Triangle
    :return: None
    """
    expected_response = "The Area of the Triangle is `4.0` units"
    actual_response = area_fixture.area_of_triangle()
    assert actual_response == expected_response


def test_area_of_circle(area_fixture) -> None:
    """
    Unit Test for Area of Circle
    :return: None
    """
    expected_response = "The Area of the Circle is `12.57` units"
    actual_response = area_fixture.area_of_circle()
    assert actual_response == expected_response


def test_area_of_square(area_fixture) -> None:
    """
    Unit Test for Area of Square
    :return: None
    """
    expected_response = "The Area of the Square is `9` units"
    actual_response = area_fixture.area_of_square()
    assert actual_response == expected_response


def test_area_of_rectangle(area_fixture) -> None:
    """
    Unit Test for Area of Rectangle
    :return: None
    """
    expected_response = "The Area of the Rectangle is `12` units"
    actual_response = area_fixture.area_of_rectangle()
    assert actual_response == expected_response
