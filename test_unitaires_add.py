import pytest
from server import checkPlaces


@pytest.mark.parametrize("placesRequired, numberOfPlaces, points, result", [
    (13, 1, 20, False),  # placeRequired > 12
    (10, 8, 20, False),  # placeRequired > numberOfPlaces
    (10, 12, 9, False),  # placeRequired > points
    (10, 12, 12, True),  # every conditions lead to success
])
def test_checkPlaces(placesRequired, numberOfPlaces, points, result):
    """
    for testing that the reservation is ok or not in several case studies
    beforehand, all the conditions have been extracted to checkPlaces function
    then, we test the function step by step each time we change its changed parameters
    """
    assert checkPlaces(placesRequired, numberOfPlaces, points) == result
