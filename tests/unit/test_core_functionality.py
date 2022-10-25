def test_area_of_triangle(area_fixture) -> None:
    """
    Unit Test for Area of Triangle
    :return: None
    """
    expected_response = "The Area of the Triangle is `6.0` units"
    actual_response = area_fixture.area_of_triangle()
    assert actual_response == expected_response


def test_area_of_circle(area_fixture) -> None:
    """
    Unit Test for Area of Circle
    :return: None
    """
    expected_response = "The Area of the Circle is `78.54` units"
    actual_response = area_fixture.area_of_circle()
    assert actual_response == expected_response


def test_area_of_square(area_fixture) -> None:
    """
    Unit Test for Area of Square
    :return: None
    """
    expected_response = "The Area of the Square is `49` units"
    actual_response = area_fixture.area_of_square()
    assert actual_response == expected_response


def test_area_of_rectangle(area_fixture) -> None:
    """
    Unit Test for Area of Rectangle
    :return: None
    """
    expected_response = "The Area of the Rectangle is `28` units"
    actual_response = area_fixture.area_of_rectangle()
    assert actual_response == expected_response
