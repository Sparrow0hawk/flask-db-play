from flask.testing import FlaskClient


def test_home_header_is_home(client: FlaskClient):
    req = client.get("/home")

    assert "<h1>Home</h1>" in req.text
