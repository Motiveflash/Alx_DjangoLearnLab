Social Media API
This is a Django-based Social Media API that provides user registration, login, and token-based authentication. It serves as the foundation for building a social media platform.

Features
User registration with token generation.
User login with token retrieval.
Custom user model with additional fields:
bio: A short bio of the user.
profile_picture: A profile picture for the user.
followers: A ManyToMany relationship for tracking user followers.
Installation
Prerequisites
Python 3.8+
Django 4.x
PostgreSQL or any supported database
Pip (Python package manager)
Steps
Clone the repository:

bash
Copy code
git clone <repository-url>
cd social_media_api
Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure the .env file (if applicable):

Add database credentials, secret key, etc.
Apply migrations:

bash
Copy code
python manage.py migrate
Start the server:

bash
Copy code
python manage.py runserver
API Endpoints
1. User Registration
URL: /api/accounts/register/
Method: POST
Request Body:
json
Copy code
{
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "password123"
}
Response:
json
Copy code
{
    "token": "<token_here>",
    "user": {
        "id": 1,
        "username": "testuser",
        "email": "testuser@example.com",
        "bio": null,
        "profile_picture": null,
        "followers": []
    }
}
2. User Login
URL: /api/accounts/login/
Method: POST
Request Body:
json
Copy code
{
    "username": "testuser",
    "password": "password123"
}
Response:
json
Copy code
{
    "token": "<token_here>",
    "user": {
        "id": 1,
        "username": "testuser",
        "email": "testuser@example.com",
        "bio": null,
        "profile_picture": null,
        "followers": []
    }
}
Project Structure
markdown
Copy code
social_media_api/
├── accounts/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── social_media_api/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── requirements.txt
How to Use
Register a User:

Send a POST request to /api/accounts/register/ with the user's details.
Receive a token and user information in response.
Login a User:

Send a POST request to /api/accounts/login/ with valid credentials.
Receive a token and user information in response.
Authenticate Requests:

Use the token in the Authorization header for future requests:
makefile
Copy code
Authorization: Token <your_token>
Future Improvements
Implement user profile management (update bio, profile picture, etc.).
Add social media features (posts, comments, likes).
Improve error handling and validation.
License
This project is open-source and available under the MIT License.

