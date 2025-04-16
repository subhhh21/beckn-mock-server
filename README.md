# Beckn Mock Server

This project is a simple **Beckn Protocol mock server** built using **Flask**. It simulates an API server for the Beckn ecosystem, helping developers create and test mock Beckn-compatible services. The goal is to improve testing, integration, and onboarding with Beckn-based applications.

---

## Features
- Simple mock API server based on Beckn Protocol.
- Provides mock responses for common Beckn services like search and catalog.
- Supports testing and integration of Beckn-based services.

---

## Setup Instructions

### Prerequisites:
- Python 3.x
- `pip` (Python package installer)

Step 1: Clone this repository

```bash
git clone https://github.com/subhhh21/beckn-mock-server.git
cd beckn-mock-server

Step 2: Install the dependencies
bash
Copy
Edit
pip install -r requirements.txt

Step 3: Run the Server
bash
Copy
Edit
python app.py
The server will run at http://127.0.0.1:5000/. You can test the following endpoints:

GET /: Returns a welcome message.

POST /search: Simulates a product search and returns mock catalog data.

Example Usage:
To test the GET / endpoint:

bash
Copy
Edit
curl http://127.0.0.1:5000/
To test the POST /search endpoint:

bash
Copy
Edit
curl -X POST http://127.0.0.1:5000/search -H "Content-Type: application/json" -d '{"context": {"domain": "retail"}}'
