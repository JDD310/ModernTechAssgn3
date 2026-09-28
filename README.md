# Password Manager

A simple, secure password manager web application built with Python and Flask. It allows users to store website credentials in a local in-memory vault, view them in a browser, and remove entries when no longer needed. Password values are encrypted before storage using the Python `cryptography` library.

## Features

- Add new credentials with a title, username, and password
- View saved entries in a clean web interface
- Delete entries you no longer need
- Encrypt stored passwords before keeping them in memory
- Lightweight Flask-based web app with a simple front-end

## Tech Stack

- Python 3
- Flask
- cryptography
- pytest

## Project Structure

- `app.py` - Flask application entry point
- `password_manager.py` - password storage and encryption logic
- `templates/` - HTML templates for the UI
- `static/` - CSS styles for the app
- `tests/` - test suite for core app behavior

## Installation

1. Open a terminal in the project directory.
2. Create and activate a virtual environment:

```bash
git clone "https://github.com/JDD310/ModernTechAssgn3.git"
cd "ModernTechAssgn3"
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the web application:

```bash
python app.py
```

2. Open the app in your browser at:

```text
http://127.0.0.1:5000
```

3. Enter a title, username, and password in the form.
4. Click Save to store the credential.
5. Review your saved credentials in the list below the form.
6. Click Delete to remove an entry.

## Running Tests

To validate the application behavior:

```bash
pytest -q
```

## Notes

This project is a simple demonstration password manager intended for learning and local use. It is not a production-grade password manager and should not be used as the sole storage mechanism for sensitive credentials in a real-world system without adding stronger protections, authentication, persistence, and secure key management.
