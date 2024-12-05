from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import uuid
from datetime import datetime

app = Flask(__name__)
CORS(app)

# In-memory database (mock)
tickets = {}


# Generate a random seat number
def generate_seat():
    rows = 32
    letters = ['A', 'B', 'C', 'D']
    return f"{random.choice(letters)}{random.randint(1, rows)}"


# Create a new ticket
@app.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.json
    departure_time = data.get('departure_time')
    source = data.get('source')
    destination = data.get('destination')
    passport_id = data.get('passport_id')

    if not departure_time or not source or not destination or not passport_id:
        return jsonify({"error": "Missing required fields."}), 400

    ticket_id = str(uuid.uuid4())
    seat = generate_seat()

    ticket = {
        "ticket_id": ticket_id,
        "departure_time": departure_time,
        "source": source,
        "destination": destination,
        "seat": seat,
        "passport_id": passport_id
    }

    tickets[ticket_id] = ticket
    return jsonify(ticket), 201

@app.route('/tickets', methods=['GET'])
def get_tickets():
    return jsonify(list(tickets.values())), 200

# Cancel a ticket
@app.route('/tickets/<ticket_id>', methods=['DELETE'])
def cancel_ticket(ticket_id):
    if ticket_id in tickets:
        del tickets[ticket_id]
        return jsonify({"message": "Ticket cancelled successfully."}), 200
    return jsonify({"error": "Ticket not found."}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)