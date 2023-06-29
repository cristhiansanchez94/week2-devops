import pytest 

from quote_disp.app import app 

@pytest.fixture()
def test_client():
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client 

def test_homepage(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    
def test_healthy(test_client): 
    response = test_client.get('/health')
    assert response.status_code == 200
    assert b'healthy' in response.data
