# Django Leaderboard Project

This is a local-only Django project that implements a leaderboard system for students, with individual and team rankings.

## Setup

1.  **Prerequisites:**
    *   Python 3.x
    *   pip

2.  **Clone the repository (or use the provided code):**
    ```bash
    git clone <repository-url>
    cd leaderboard_project
    ```

3.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the database migrations:**
    ```bash
    python3 manage.py migrate
    ```

6.  **Create a superuser to access the admin panel:**
    ```bash
    python3 manage.py createsuperuser
    ```
    Follow the prompts to create a username and password.

## Running the Project

1.  **Start the development server:**
    ```bash
    python3 manage.py runserver
    ```

2.  **Access the application:**
    *   **Individual Leaderboard:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    *   **Team Leaderboard:** [http://127.0.0.1:8000/teams/](http://127.0.0.1:8000/teams/)
    *   **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Managing Data

All data (students, teams, scores, etc.) can be managed through the Django Admin interface.
