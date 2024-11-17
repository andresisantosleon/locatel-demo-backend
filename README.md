# Locatel Demo Backend

This is a Django project using Rye.

## Requirements
- Rye https://rye.astral.sh/


## Installation
1. Install Rye: https://rye.astral.sh/guide/installation/

3. Install project dependencies:
    ```bash
    rye sync
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

## Running the Project

1. Start the development server:
    ```bash
    python manage.py runserver
    ```

2. Open your browser and go to `http://127.0.0.1:8000/`.

