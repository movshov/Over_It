# Over_It
SRE Fall 2020 Group Project
##### Created By: Bar Movshovich, Danielle Beyer, and Evan DePosit


# Set UP: 
Before running our project you will first need to create a virutal environment to work in. Follow the steps listed below in the order in which they appear: 
* sudo apt update
* sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl

These commands above will install the needed software and will start both NGINX and Postgres for you. 

Next we will need to update the running Postgres database server with artifacts that Django needs to run python applications. 
* sudo -u postgres psql

You will see a PostgreSQL prompt. From here create a database with the following command: 

* CREATE DATABASE sreproject;

Next create a database user for the project. 
* CREATE USER sreprojectuser WITH PASSWORD '<*password-goes-here*>';

The next three commands are recommended by the django project to help save you time and effort when interacting with Postgres. Do them now to save yourself effor later. 
* ALTER ROLE sreprojectuser SET client_encoding TO 'utf8';
* ALTER ROLE sreprojectuser SET default_transaction_isolation TO 'read committed';
* ALTER ROLE sreprojectuser SET timezone TO 'UTC';

Next give the sreprojectuser access to administer the new database. 
* GRANT ALL PRIVILEGES ON DATABASE sreproject TO sreprojectuser;

Then exit psql by entering "\q" at the prompt. Postgres is now set up so that Django can connect and manage its database information. 

Next we will need to install your Python requirements within a virtual environment for easier management. To do this type the following commands: 
* sudo -H pip3 install --upgrade pip
* sudo -H pip3 install virtualenv

Within your project directory, create a Python virtual environment by typing the following command: 
* virtualenv sreprojectenv

This will create a directory called sreprojectenv within your sreprojectdir directory. Inside, it will install a local version of Python and a local version of pip which you will use to install and configure an isolated Python environment for the project.Before installing the project’s Python requirements activate the virtual environment by typing:

* source sreprojectenv/bin/activate

By the way, be sure to run this command whenever you login to your VM so that you are operating in the correct environment.
Next install Django, Gunicorn, and the psycopg2 PostgreSQL adaptor by typing:
* pip install django gunicorn psycopg2-binary

You now have all of the software needed to start a Django project.




