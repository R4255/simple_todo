Simple Todo API
Simple Todo is a Django REST Framework-based API for managing notes. It provides endpoints for creating, retrieving, updating, and querying notes.
Features

Create new notes
Retrieve existing notes
Update notes
Query notes by title
Swagger UI for API documentation

Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.8+
pip (Python package manager)
virtualenv (recommended for creating isolated Python environments)

Setting Up the Project Locally
Follow these steps to set up and run the project on your local machine:

Clone the repository:
Copygit clone https://github.com/yourusername/simple-todo.git
cd simple-todo

Create and activate a virtual environment:
Copypython -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required dependencies:
Copypip install -r requirements.txt

Apply database migrations:
Copypython manage.py migrate

Create a superuser (optional, for admin access):
Copypython manage.py createsuperuser

Run the development server:
Copypython manage.py runserver


The API should now be accessible at http://localhost:8000/api/.
API Endpoints

POST /api/notes/: Create a new note
GET /api/notes/<id>/: Retrieve a specific note
PUT /api/notes/<id>/update/: Update a specific note
GET /api/notes/query/?title=<substring>: Query notes by title

API Documentation
Swagger UI documentation is available at http://localhost:8000/swagger/ when the server is running.
Running Tests
To run the test suite:
Copypython manage.py test
