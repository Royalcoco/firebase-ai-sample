import pytest
from app import app, hash_password, users

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_register(client):
    rv = client.post('/register', json={
        "username": "testuser",
        "password": "testpassword",
        "ping_time": 100
    })
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert json_data['status'] == 'success'

def test_withdraw(client):
    users.insert_one({
        "username": "testuser",
        "password_hash": hash_password("testpassword"),
        "2fa_secret": pyotp.random_base32(),
        "ping_time": 100
    })
    rv = client.post('/withdraw', json={
        "user": "testuser",
        "password": "testpassword",
        "2fa_code": pyotp.TOTP(users.find_one({"username": "testuser"})["2fa_secret"]).now(),
        "ping_time": 100
    })
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert json_data['status'] == 'success'
