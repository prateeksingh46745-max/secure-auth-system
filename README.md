# Secure Authentication System

A backend authentication system built with Flask, featuring JWT-based session management and bcrypt password hashing. Includes user registration, login, and protected route access.

## Features

- User registration with secure password hashing (bcrypt)
- Login with JWT token generation
- Protected routes requiring valid JWT authentication
- PostgreSQL database integration via SQLAlchemy

## Tech Stack

- **Backend:** Python, Flask
- **Database:** PostgreSQL
- **ORM:** Flask-SQLAlchemy
- **Authentication:** Flask-JWT-Extended
- **Password Hashing:** bcrypt

## Project Structure
Secure_auth/

├── app.py              # Flask app entry point
├── config.py           # Configuration and environment loading
├── models.py           # Database models (User)
├── routes.py           # API endpoints
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
└── .env                # Environment variables (not committed)

## API Endpoints

| Method | Endpoint    | Description                  | Auth Required |
|--------|------------|-------------------------------|----------------|
| POST   | `/register` | Register a new user          | No             |
| POST   | `/login`    | Login and receive JWT token  | No             |
| GET    | `/profile`  | Get logged-in user's profile | Yes (JWT)      |

## Setup Instructions

1. Clone the repository
```bash
git clone <your-repo-url>
cd Secure_auth
```

2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory

```env
DATABASE_URL=postgresql://username:password@localhost:5432/auth_db
JWT_SECRET_KEY=your_secret_key
```

5. Run the application
```bash
python app.py
```

## How It Works

1. **Registration:** User submits username, email, and password. Password is hashed using bcrypt before being stored in PostgreSQL.
2. **Login:** User submits email and password. bcrypt verifies the password against the stored hash. If valid, a JWT access token is issued.
3. **Protected Access:** Requests to `/profile` must include the JWT token in the Authorization header (`Bearer <token>`). The server validates the token before returning user data.

## Screenshots

### Register Endpoint
![Register](screenshots/register.png)

### Login Endpoint
![Login](screenshots/login.png)

### Protected Route
![Profile](screenshots/profile.png)

## Testing

Tested using Postman:
- Registration returns `201 Created` on success
- Login returns `200 OK` with a valid JWT token
- Accessing `/profile` with a valid token returns user data
- Accessing `/profile` without a token returns `401 Unauthorized`

## Author

Prateek Singh Chouhan
B.Tech CSE | Amity University Jaipur