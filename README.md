## Cesar's Milestone Project
## Working in Atom
## Virtual environment Env : Env\Scripts\activate
## Heroku Deployment perfect

for heroku deployment without cloud 9:
create a new heroku app and link to github Repository.
all requirements need to be installed.
psycopg2 module needs to be installed and in requirements.
dj_database_url needs to be installed and in requirements and settings as module.
Procfile needs to have the right name for the WSGI_APPLICATION = 'RTech.wsgi.application'.
in heroku install the posgres Database
in heroku dashboard create the variables for PORT and IP.
use heroku ps:scale web=1 for set up.
use heroku cli >heroku congig  to copy the database address
change settings to change the Database variable.

## things to do
* the model of post need to have Boolean values to bring 'active', 'fixed', 'fixed date', 'in works', 'free', 'service_1', 'service_2', 'service_2', 'administrator'
  the values will update the posts and create lists with filtered posts
* if fixed record the date when fixed
* add project page with details and blog
* blog model with foreign key == project primary key
* if administrator user name == logged user gets modify access, if not just view
* the delete function needs to have an extra security step to avoid wrong deletions
* delete function not necessary as post will go to fixed list
* the model needs to have Boolean values to update services on every post
* need a button on every post to add to "request this", python functionality to save posts ids in  personal list
  write to a file ?? use the data base to store my favorites??
* add to cart all services requested
* if I request add to the cart
* create graphs that count details in the projects, services, language, active, fixed, done, time table


* Html
* CSS
* JavaScript
* chart.js
* Python
* Django
* Sql databases
* Ecommerce
* Travis
* Heroku
* Amazon services
* Github

## wireframes
## user stories
## data base schema
## design
## logic
