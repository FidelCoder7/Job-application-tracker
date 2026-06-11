# Job Application Tracker

A production-style FastAPI backend for managing job applications, tracking application status, and analyzing job search performance.

Built with FastAPI, SQLAlchemy, JWT Authentication, Pytest, and GitHub Actions.


## Features

- User Registration & Login
- JWT Authentication
- Password Hashing
- CRUD Operations for Job Applications
- Dashboard Analytics
- User Ownership Protection
- Automated Testing with Pytest
- CI/CD with GitHub Actions


## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT
- Pytest
- GitHub Actions

## API Endpoints

### Authentication

POST /auth/register

POST /auth/login

GET /auth/me

### Applications

POST /applications

GET /applications

GET /applications/{id}

PUT /applications/{id}

DELETE /applications/{id}

### Dashboard

GET /dashboard/stats


## Installation

git clone https://github.com/yourusername/job-application-tracker.git

cd job-application-tracker

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

cp .env.example .env

uvicorn main:app --reload


## Testing

pytest -v


## Future Improvements

- PostgreSQL Support
- Docker Deployment
- Frontend Dashboard
- Email Notifications
- Advanced Analytics

