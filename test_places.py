import pytest
from server import loadClubs
from server import loadCompetitions


def test_places_maximum_ok(client):
    response = client.post("purchasePlaces",
                           data={"places": 2, "competition": "Spring Festival", "club": "Simply Lift"})
    assert response.status_code == 200


def test_places_maximum_nok(client):
    response = client.post("purchasePlaces",
                           data={"places": 26, "competition": "Spring Festival", "club": "Simply Lift"})
    assert response.status_code == 401


def test_points_decrement_ok(client):
    clubs = loadClubs()
    simplylist = clubs[0]
    assert simplylist["points"] == "13"
    response = client.post("purchasePlaces",
                           data={"places": 2, "competition": "Spring Festival", "club": "Simply Lift"})
    assert response.status_code == 200
    clubs = loadClubs()
    simplylist = clubs[0]
    assert simplylist["points"] == "11"


"""
def test_places_decrement_ok(client):
    clubs = loadClubs()
    competitions = loadCompetitions()
    springfestvival = competitions[0]
    assert springfestvival["numberOfPlaces"] == 25
    response = client.post("purchasePlaces",
                           data={"places": 2, "competition": "Spring Festival", "club": "Simply Lift"})
    assert response.status_code == 200
    assert springfestvival["numberOfPlaces"] == 23
    """


def test_points_decrement_nok(client):
    clubs = loadClubs()
    simplylist = clubs[0]
    assert simplylist["points"] == "13"
    response = client.post("purchasePlaces",
                           data={"places": 26, "competition": "Spring Festival", "club": "Simply Lift"})
    assert response.status_code == 401
    assert simplylist["points"] == "13"


def test_points_minimum_ok(client):
    response = client.post("purchasePlaces",
                           data={"places": 2, "competition": "Spring Festival", "club": "Simply Lift"})
    assert response.status_code == 200


def test_points_minimum_nok(client):
    response = client.post("purchasePlaces",
                           data={"places": 26, "competition": "Spring Festival", "club": "Simply Lift"})
    assert response.status_code == 401
