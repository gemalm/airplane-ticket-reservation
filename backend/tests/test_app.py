import json
import pytest
from app import app  # Import your Flask app

@pytest.fixture
def client():
    """Set up the Flask test client."""
    with app.test_client() as client:
        yield client

def test_create_ticket(client):
    """Test creating a new ticket."""
    ticket_data = {
        "departure_time": "2024-12-31T10:00:00",
        "source": "New York",
        "destination": "London",
        "passport_id": "P1234567"
    }
    response = client.post('/tickets', data=json.dumps(ticket_data), content_type='application/json')
    assert response.status_code == 201
    data = response.get_json()
    assert data["source"] == "New York"
    assert data["destination"] == "London"
    assert data["passport_id"] == "P1234567"
    assert "ticket_id" in data

def test_get_tickets(client):
    """Test retrieving all tickets."""
    response = client.get('/tickets')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

def test_cancel_ticket(client):
    """Test canceling a ticket."""
    # First, create a ticket
    ticket_data = {
        "departure_time": "2024-12-31T10:00:00",
        "source": "New York",
        "destination": "London",
        "passport_id": "P1234567"
    }
    create_response = client.post('/tickets', data=json.dumps(ticket_data), content_type='application/json')
    assert create_response.status_code == 201
    ticket_id = create_response.get_json()["ticket_id"]

    # Now, cancel the ticket
    cancel_response = client.delete(f'/tickets/{ticket_id}')
    assert cancel_response.status_code == 200
    assert cancel_response.get_json()["message"] == "Ticket cancelled successfully."

    # Verify the ticket is no longer available
    get_response = client.get('/tickets')
    tickets = get_response.get_json()
    assert not any(ticket["ticket_id"] == ticket_id for ticket in tickets)