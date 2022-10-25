import pytest
from area_plane_shapes.core import AreaPlaneShapes


@pytest.fixture(scope="class")
def area_fixture():
    return AreaPlaneShapes(radius=5,
                           base=3,
                           height=4,
                           side=7)


@pytest.fixture(scope="class")
def area_fixture_invalid_height():
    return AreaPlaneShapes(radius=5,
                           base=3,
                           height="INVALID",
                           side=7)


@pytest.fixture(scope="class")
def area_fixture_none_radius():
    return AreaPlaneShapes(
        base=3,
        height=4,
        side=7)


@pytest.fixture(scope="class")
def area_fixture_none_side_height():
    return AreaPlaneShapes(radius=5,
                           base=3
                           )
