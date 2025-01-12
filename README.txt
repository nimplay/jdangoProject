Command for start>

virtual machine:

- python3 -m venv venv
- source venv/bin/activate

create new app (Feature):

- python manage.py startapp [NEW COMPONENT NAME]

database:
- sudo apt install mysql-server #install Database SErver
- python manage.py migrate  # Make a migration
- python mydb.py # Run data base first time
- mysql -u root -p # look data base working
- sudo service mysql status # Look database status
- sudo mysql -u root
- sudo service mysql restart # Restart Data base
- sudo service mysql start

