# Fitness Tracker API (Django REST Framework)

This is a scaffolded Django + DRF project for a Fitness Tracker API (activities, users).
Files were generated automatically to help you start coding quickly. Edit settings and add migrations before running.

## Quickstart (local)
1. Create virtualenv and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Make migrations and migrate:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```
5. Run server:
   ```bash
   python manage.py runserver
   ```

## Notes
- Configure `settings.py` SECRET_KEY and DEBUG appropriately for production.
- Deployment: Procfile for Heroku included; adjust DATABASE config for production.
