import pytest
import copy  # for permitting copying variable with value at first instancing only
from server import app  # for configuring python fixture at end otherwise doesn't work
from server import clubs  # for loading clubs instead of loadClubs() like it's in server.py


def test_places_reserved_inferior_12_ok(client):
    """
    for testing that the reservation under 12 places is ok
    at the end, the remaining number of points will be 13-3 == 10, for simply lift
    """
    response = client.post("purchasePlaces",
                           data={"places": 3, "competition": "Fall Classic", "club": "Simply Lift"})
    assert response.status_code == 200


def test_places_reserved_inferior_12_nok(client):
    """
    for testing that the reservation over 12 places is not ok
    at the end, the remaining number of points will be 10-0 == 10, for simply lift
    """
    response = client.post("purchasePlaces",
                           data={"places": 13, "competition": "Fall Classic", "club": "Simply Lift"})
    assert response.status_code == 401


def test_points_decrement_ok_points_limit_ok(client):
    """
    for testing that the decrement of points for selected club is ok
    if the decrement is working, it means that the points limit isn't reached
    at the end, the remaining number of points will be 10-3 == 7, for simply lift
    """
    simply_lift_entry = clubs[0]
    simply_lift_entry_points = copy.deepcopy(simply_lift_entry["points"])
    response = client.post("purchasePlaces",
                           data={"places": 3, "competition": "Fall Classic", "club": "Simply Lift"})
    assert response.status_code == 200
    simply_lift_output = clubs[0]
    assert simply_lift_output["points"] == simply_lift_entry_points - 3


def test_points_decrement_nok_points_limit_nok(client):
    """
    for testing that the decrement of points for selected club is not ok
    it's done by testing that the club points can't be spent over its limit
    at the end, the remaining number of points will be 7-0 == 7, for simply lift
    """
    simply_lift_entry = clubs[0]
    simply_lift_entry_points = copy.deepcopy(simply_lift_entry["points"])
    response = client.post("purchasePlaces",
                           data={"places": 8, "competition": "Fall Classic", "club": "Simply Lift"})
    assert response.status_code == 401
    simply_lift_output = clubs[0]
    assert simply_lift_output["points"] == simply_lift_entry_points


def test_competition_places_limit_ok_nok(client):
    """
    for testing that the competition places can't be reserved over its limit
    at the beginning, selected competition had same amount of club points, according to json
    at the end, the remaining number of points will be 7-7 == 0 for simply lift, and 0 places for iron temple
    """
    response = client.post("purchasePlaces",
                           data={"places": 7, "competition": "Fall Classic", "club": "Simply Lift"})
    assert response.status_code == 200
    response = client.post("purchasePlaces",
                           data={"places": 4, "competition": "Fall Classic", "club": "Iron Temple"})
    assert response.status_code == 401


@pytest.fixture
def client():
    client = app.test_client()
    return client
