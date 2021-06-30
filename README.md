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
  - You will need a `master.key` file in the root (`.`) of the project 
  - This key is not public on GitHub (ask a colleague for it).
  - See/edit secrets with `EDITOR=vi python3 manage.py edit_secrets`


# Test the application
  - Collect static files: `python3 manage.py collectstatic`
  - Run tests: `python3 manage.py test`