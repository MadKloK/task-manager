# Django Task Manager

A task management web application built with Django.

This project was created to practice Django development concepts such as authentication, CRUD operations, database design, testing, Docker, and PostgreSQL integration.

## Features

* User registration and authentication
* Create, update, and delete tasks
* Task priorities and statuses
* Due dates
* Search and filtering
* Pagination
* PostgreSQL support
* Dockerized deployment
* Automated tests with GitHub Actions

## Tech Stack

* Python
* Django
* PostgreSQL
* Bootstrap 5
* Docker
* Gunicorn

## Installation

Clone the repository:

```bash
git clone https://github.com/MadKloK/task-manager.git
cd task-manager
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

## Running Tests

```bash
python manage.py test
```

## Future Improvements

* Task categories and tags
* REST API with Django REST Framework
* Email notifications
* Team collaboration features

## License

This project is open source and available under the MIT License.
