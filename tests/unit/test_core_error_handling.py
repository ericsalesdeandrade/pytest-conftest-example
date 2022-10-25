
def test_area_circle_none_radius(area_fixture_none_radius) -> None:
    """
    Unit Test for Area of Circle with None Radius
    :return: None
    """
    expected_response = "Area Unavailable. " \
                        "Please initialise Class with `Radius`"
    actual_response = area_fixture_none_radius.area_of_circle()
    assert actual_response == expected_response


def test_area_rectangle_none_side_height(area_fixture_none_side_height) -> None:
    """
    Unit Test for Area of Rectangle with None Side and Height
    :return: None
    """
    expected_response = "Area Unavailable. " \
                        "Please initialise Class with `Side` and `Height`"
    actual_response = area_fixture_none_side_height.area_of_rectangle()
    assert actual_response == expected_response
