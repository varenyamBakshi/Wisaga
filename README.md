# Wisaga
Building a platform for managing club's learning resources

# Requirements
python 3.8.0

postgresql-12
install using apt-repository from https://www.postgresql.org/download/

psycopg2
it also requires other packages-
->python-dev
->libpq-dev
for ubuntu they can be installed as 
`sudo apt-get update -y`

`sudo apt-get install -y python-dev`

`sudo apt-get install -y libpq-dev`

then run
`pip install psycopg2`

if any error occur check https://www.psycopg.org/docs/install.html of google it XD.

To integrate the database to the django project follow the below link.
https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database
This tutorial is for MySQL where ever necessary change it with postgre sql.
