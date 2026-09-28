import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app(testing=True)
    with app.test_client() as client:
        yield client


def test_home_page_loads(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Password Manager' in response.data


def test_can_add_and_list_entry(client):
    response = client.post('/entries', data={
        'title': 'GitHub',
        'username': 'alice',
        'password': 'supersecret',
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'GitHub' in response.data
    assert b'alice' in response.data


def test_can_delete_entry(client):
    client.post('/entries', data={
        'title': 'GitHub',
        'username': 'alice',
        'password': 'supersecret',
    })

    response = client.post('/entries/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'GitHub' not in response.data
