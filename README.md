# Blog Site

A full-featured blog web application built with Flask. Users can register, create posts, update their profiles, and reset passwords via email.

## Features

- **User Authentication** — Register, login, logout with hashed passwords (Bcrypt)
- **User Profiles** — Upload profile pictures, update username & email
- **Blog Posts** — Create, read, update, and delete posts (CRUD)
- **Pagination** — Paginated post listings
- **Password Reset** — Token-based password reset via email (Gmail SMTP)
- **Error Handling** — Custom 403, 404, and 500 error pages

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Flask, Flask-SQLAlchemy, Flask-Login, Flask-Bcrypt, Flask-Mail |
| Database | SQLite |
| Frontend | Jinja2 Templates, CSS |
| Auth | Flask-Login + Bcrypt |

## Project Structure

```
Flask_first/
├── run.py                  # Application entry point
├── flasktut/
│   ├── __init__.py         # App factory & extensions
│   ├── config.py           # Configuration (env variables)
│   ├── models.py           # User & Post database models
│   ├── main/               # Home & about routes
│   ├── users/              # Auth, account, password reset
│   ├── posts/              # CRUD for blog posts
│   ├── errors/             # Custom error handlers
│   ├── static/             # CSS & profile pictures
│   └── templates/          # Jinja2 HTML templates
└── instance/
    └── site.db             # SQLite database (gitignored)
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/PranshuNalwa/Blog-Site.git
   cd Blog-Site
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask flask-sqlalchemy flask-bcrypt flask-login flask-mail python-dotenv itsdangerous pillow flask-wtf
   ```

4. **Set up environment variables** — Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your_secret_key_here
   SQLALCHEMY_DATABASE_URI=sqlite:///site.db
   EMAIL_USERNAME=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

   The app will be available at `http://localhost:5000`.

## Environment Variables

| Variable | Description |
|---|---|
| `SECRET_KEY` | Secret key for session management & token generation |
| `SQLALCHEMY_DATABASE_URI` | Database connection string |
| `EMAIL_USERNAME` | Gmail address for sending password reset emails |
| `EMAIL_PASSWORD` | Gmail app password |

## License

This project is open source and available under the [MIT License](LICENSE).
