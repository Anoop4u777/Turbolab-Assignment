This is a Assignment project that creates a csv file as an output in the data folder.


Steps to run the project.

Create a virtual environment using python.
python3 -m venv environment-name

Install the requirements from the requirements file.
ie, pip install -r requirements.txt

Run the migrations for the database.
python manage.py migrate

Run the project
python manage.py runserver


NOTE: Both the below will only run if the python environment is activated.

In another tab run celery worker for background processing.
python -m celery -A Assignment worker -l info

In another tab run celery beat for periodic task processing.
python -m celery -A Assignment beat -l info

NOTE:
Make sure the redis-server is running in the system and is active.
If not run redis-server