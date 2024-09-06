# Simple Todo API

Simple Todo is a Django REST Framework-based API for managing notes. It provides endpoints for creating, retrieving, updating, and querying notes.

## Features

- Create new notes
- Retrieve existing notes
- Update notes
- Query notes by title
- Swagger UI for API documentation

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8+
- pip (Python package manager)
- virtualenv (recommended for creating isolated Python environments)

## Setting Up the Project Locally

Follow these steps to set up and run the project on your local machine:

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/simple-todo.git
   cd simple-todo
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```
   python manage.py migrate
   ```

5. Create a superuser (optional, for admin access):

   ```
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```
   python manage.py runserver
   ```

The API should now be accessible at `http://localhost:8000/api/`.

## API Endpoints

- `POST /api/notes/`: Create a new note
- `GET /api/notes/<id>/`: Retrieve a specific note
- `PUT /api/notes/<id>/update/`: Update a specific note
- `GET /api/notes/query/?title=<substring>`: Query notes by title

## API Documentation

Swagger UI documentation is available at `http://localhost:8000/swagger/` when the server is running.

## Running Tests

To run the test suite:

```
python manage.py test
```
