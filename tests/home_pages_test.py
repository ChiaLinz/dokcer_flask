"""This test the homepage"""


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/index")
    assert response.status_code == 200
    assert b"Chia-Lin's HomePage" in response.data

def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"Chia-Lin's About Page" in response.data


