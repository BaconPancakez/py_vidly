
# Vidly Django Project

This is the Vidly project, a Django-based web application deployed on Heroku. The project showcases a simple video rental service where users can explore movies and related data through an API. 

### Live Demo

You can view the project live here: [Vidly Project on Heroku](https://guarded-inlet-90633-518ffea8ece3.herokuapp.com/)

## Project Overview

The Vidly project is a Django web application that manages movies and allows users to perform CRUD (Create, Read, Update, Delete) operations on them. It also includes an API to interact with the movie data programmatically.

### Main Features:
- Movie management system with an intuitive web interface.
- RESTful API for movies (created using Django Rest Framework).
- Fully functional admin panel.
- Authentication and user management using Django's built-in tools.

## Technologies Used

- **Backend**: Django 5.1.2 (Python framework)
- **Frontend**: HTML/CSS (Django Templates)
- **Database**: SQLite (default configuration, easily configurable for PostgreSQL or MySQL)
- **Deployment**: Heroku (includes Whitenoise for serving static files)

## Quick Start

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/BaconPancakez/py_vidly
   cd vidly
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your local environment (create a `.env` file if needed) and apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Running Locally with Heroku

To push this application to Heroku, follow these steps:
1. Login to Heroku:
   ```bash
   heroku login
   ```

2. Create a Heroku application:
   ```bash
   heroku create
   ```

3. Deploy the code to Heroku:
   ```bash
   git push heroku main
   ```

4. Apply migrations:
   ```bash
   heroku run python manage.py migrate
   ```

5. Access the app:
   ```bash
   heroku open
   ```

## Settings Configuration

The Django `settings.py` file contains important configurations such as:

- `DEBUG` mode (ensure to turn it off in production).
- `ALLOWED_HOSTS` includes your Heroku domain.
- `DATABASES` is set up to use SQLite locally, but it can easily be configured for other databases.

### Example:

```python
ALLOWED_HOSTS = ['guarded-inlet-90633-518ffea8ece3.herokuapp.com']
DEBUG = True  # Make sure this is False in production
```

## Deployment

This project is deployed on [Heroku](https://www.heroku.com/), which is a cloud platform for building, running, and operating applications entirely in the cloud. The deployment includes serving static files using **Whitenoise** middleware.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License.
