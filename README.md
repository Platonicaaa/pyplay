# pyplayy

Sandbox project for playing with the capabilities of Django Framework.

# Requirements:

- ### [pipenv](https://formulae.brew.sh/formula/pipenv)
- ### PostgreSQL
- ### Heroku CLI
    - Just for deployment purposes

# Run the app

- Have a `pyplayy` database created in Postgres.
- `pipenv install` to fetch packages
- `pipenv shell` to launch virtual env
- `python3 manage.py migrate`
- `python3 manage.py runserver` and you're good to go!

# View/Edit application secrets

- Ask one of the devs for the `.env` file

# Test the application

- Collect static files: `python3 manage.py collectstatic`
- Run tests: `python3 manage.py test`

# Project Apps Description

- `acconts`: custom user accounts used inside the application
- `auctions`: auction/bidding logic
- `polls`: leftover from the original Django tutorial. Will be removed later, at the moment it's still useful for testing
- `pyplayy`: the main module