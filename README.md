# Mystery-Tour

This web application was developed in Python using the Django framework

Three end-user categories exist for this project:
  - Students
  - Game Keepers
  - Developers

Students - these users have the ability to take part in treasure hunts following one of a number of routes: General, Accessibility and Computer Science. Customised routes can also be created by users. When they wish to start the game, they are asked to enter a team name, the number of team mebers playing and their desired routes. They are then presented with a page explaining how to play before the first clue is presented. For each task, when answered correctly, a score of 10 is awarded. When answered incorrectly, 5 points are deducted. The user may skip a task if they wish. Upon completing the task for the final location for their selected route, an end page shows the users their score and allows them to view the leaderboards. The leaderboards can be viewwed with scores for all routes and the option to filter the list by route is also avaiable.

Game Keepers - these users are able to log in to the Django Administrator site. This provides an interface to access the database models. They can therefore manage the resources of the application by creating, editing or deleting records in any table.

Developers - members of the development team have access to the shared code repository hosted on GitHub.

--------------------------------------------------------

Requirements.txt must be run to install the prerequisites:

PIL

django-filter

asgiref==3.2.3

certifi==2019.11.28

chardet==3.0.4

dj-database-url==0.5.0

Django==3.0.3

django-crispy-forms==1.8.1

django-heroku==0.3.1

idna==2.9

psycopg2==2.8.4

pytz==2019.3

requests==2.23.0

sqlparse==0.3.0

urllib3==1.25.8

whitenoise==5.0.1

--------------------------------------------------------

Instructions to run a local copy
1. Navigate to technical-documents directory in a Python Virtual Environment with all of requirements.txt installed
2. python manage.py runserver
3. Navigate to localhost (likely 127.0.0.1:8000) in a web browser
4. If changes to database models are made:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver
  
  
Hosted copy:
https://exetermysterytour.herokuapp.com/


