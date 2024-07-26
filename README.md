# Reddit-Style News Site

This project is a Reddit-style news website created using Django. Users can create, read, update, and delete posts, and also comment on posts. The project uses MongoDB for data storage and integrates with Heroku for deployment.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Pumpkinpoem/pp4-reddit-style-news-site.git
    cd pp4-reddit-style-news-site
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:
    - Make sure MongoDB is installed and running on your machine.
    - Configure the connection to your MongoDB instance in `reddit_news/settings.py`.

5. Run the migrations:
    ```sh
    python manage.py migrate
    ```

6. Load initial data:
    ```sh
    python manage.py loaddata categories.json
    ```

7. Create a superuser to access the admin panel:
    ```sh
    python manage.py createsuperuser
    ```

8. Start the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

- Access the website at `http://127.0.0.1:8000/`.
- Log in with your superuser account to create and manage posts and comments.
- Use the admin panel at `http://127.0.0.1:8000/admin/` for advanced management.

## Features

- User authentication and authorization
- Create, read, update, and delete posts
- Comment on posts
- Upvote and downvote posts
- Admin panel for managing content
- Responsive design

## Technologies

- **Backend**: Django, MongoDB
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Heroku

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
