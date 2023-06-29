import pytest 
from quote_gen.app import app 

quotes = [
        "The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela",
        "The way to get started is to quit talking and begin doing. -Walt Disney",
        "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking. -Steve Jobs",
        "If life were predictable it would cease to be life, and be without flavor. -Eleanor Roosevelt",
        "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. -Oprah Winfrey",
        "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. -James Cameron",
    ]

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
    
def test_gen(test_client):
    response = test_client.get('/quote')
    assert response.status_code == 200
    assert response.text in quotes