Task Management Application:
This is a simple task management application built with Django. It helps users create, update, and track their tasks.
vercel app link: https://taskmanagerapplication-omega.vercel.app/

Features:
Create, edit, and delete tasks
Filter tasks by status 

Setup Instructions:
Prerequisites:-
Python installed (version 3.8 or above)
Git installed

Steps:
Clone the repository:-
cmd:git clone https://github.com/yourusername/task-management-app.git
cmd:cd task-management-app

Create a virtual environment and activate it:
cmd:python -m venv env
cmd:env\Scripts\activate

Install Django and other required dependencies:
First, install Django:-
cmd:pip install django
Then, install the remaining dependencies from requirements.txt:-
cmd: pip install -r requirements.txt

Run database migrations:
cmd:python manage.py migrate
Create a superuser (admin):
cmd:python manage.py createsuperuser

Run the development server:
cmd:python manage.py runserver
Access the app: Open http://127.0.0.1:8000/ in your browser.

Deployment Instructions
You can deploy the app using any hosting service (e.g., Vercel or Heroku).

Push your code to a remote Git repository.
Follow the hosting provider’s instructions for Django deployment.