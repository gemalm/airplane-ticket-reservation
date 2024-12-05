# Airplane Ticket Reservation System

An airplane ticket reservation system built using **Flask** (Python) for the backend, **Vue.js** for the frontend, and Docker for containerization. This application provides a RESTful API for managing flight ticket reservations and a user-friendly interface for booking, viewing, and canceling tickets.

---

## 🚀 Features

- **Book Tickets**: Users can book flight tickets by providing source, destination, departure time, and passport ID.
- **View Tickets**: A list of all booked tickets is available.
- **Cancel Tickets**: Users can cancel a specific ticket by its ID.
- **Dockerized**: Fully containerized using Docker and Docker Compose for ease of setup and deployment.
- **RESTful API**: Exposes endpoints to manage tickets programmatically.

---

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: Vue.js (JavaScript)
- **Database**: In-memory (Python dictionary) for simplicity
- **Containerization**: Docker, Docker Compose
- **Testing**: Pytest
- **CI/CD**: GitHub Actions

---

## 📂 Project Structure

```plaintext
airplane-ticket-reservation/
├── backend/
│   ├── app.py             # Flask app (backend)
│   ├── requirements.txt   # Python dependencies
│   ├── Dockerfile         # Dockerfile for the backend
│   ├── tests/
│       ├── __init__.py    # Test package init
│       ├── test_app.py    # Test cases for the backend
├── frontend/
│   ├── index.php          # Frontend entry point
│   ├── Dockerfile         # Dockerfile for the frontend
│   ├── assets/
│       ├── app.js         # Vue.js app logic
│       ├── styles.css     # CSS for styling
├── .github/
│   ├── workflows/
│       ├── test-backend.yml   # GitHub Actions for CI
├── docker-compose.yml     # Docker Compose configuration
├── README.md              # Project documentation
```
## ⚙️ Setup Instructions
Prerequisites
- Docker
- Docker Compose
- Python 3.9+ (for local development and testing)

## 🐳 Run with Docker
Clone the repository:
```sh
git clone https://github.com/your-username/airplane-ticket-reservation.git
cd airplane-ticket-reservation
```
Build and start the containers:
```sh
docker-compose up --build
```
Access the application:
- Frontend: http://localhost:8080
- Backend API: http://localhost:5001

## 🖥️ Local Development (Backend)
Navigate to the backend directory:

```sh
cd backend
```
Install dependencies:
```sh
pip install -r requirements.txt
```
Run the Flask app:
```sh
flask run --host=0.0.0.0 --port=5001
```
Run Tests:
```sh
PYTHONPATH=backend pytest backend/tests
```

## 📋 API Endpoints
Base URL: http://localhost:5001
1. Create a flight ticket:  
Endpoint: /tickets  
Method: POST  
Body:
```json
{
  "departure_time": "2024-12-31T10:00:00",
  "source": "New York",
  "destination": "London",
  "passport_id": "P1234567"
}
```
2. Get All Tickets:  
Endpoint: /tickets  
Method: GET  
Response:
```json
[
  {
    "ticket_id": "abc123",
    "departure_time": "2024-12-31T10:00:00",
    "source": "New York",
    "destination": "London",
    "seat": "B15",
    "passport_id": "P1234567"
  }
]
```
3. Cancel Ticket:  
Endpoint: /tickets/<ticket_id>  
Method: DELETE  
Response:
```json
{
  "message": "Ticket cancelled successfully."
}
```

## ✅ Testing
To run the backend tests:

Navigate to the backend directory:
```sh
cd backend
```
Run the tests:
```sh
PYTHONPATH=backend pytest tests
```

## 🚀 CI/CD with GitHub Actions
This project uses GitHub Actions to automate testing on every push or pull request. The configuration is in .github/workflows/test-backend.yml.

## 🛠️ Future Enhancements
- Implement a persistent database (e.g., PostgreSQL, MySQL).
- Add authentication for secure ticket management.
- Expand frontend functionality using Vue.js components.
- Deploy the application to cloud providers like AWS, Azure, or Heroku.

## 📄 License
This project is licensed under the MIT License.

## 📧 Contact
If you have any questions or feedback, feel free to contact [me@gemalopez.es].