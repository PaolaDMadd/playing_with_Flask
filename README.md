# From class exercise Kai_Paola_using_Flask
The initial project was to implement a virtual trainers collection/library using the following requirements:

### Create a Flask API
* You can choose what it does!
* Your API should respond to at least one GET and one POST request
* Add at least one extension eg. a database connection or an email service
* Follow documentation to add some tests using [pytest] (https://pytest-flask.readthedocs.io/en/latest/features.html)

## Improvements
I changed the structure of the project:
* using a mvc approach 
* added functionalities: 
    [ ]email 
    [x]database connection
* test suit(working on progress)

## To run the app
`pipenv install -r requirements.txt`
`pipenv shell`
Tell terminal which application to work with:
`export FLASK_APP=server.py (Linux/MacOS/GitBash)`
`set FLASK_APP=server.py (Windows Command Prompt)`
`$env:FLASK_APP = "server.py" (PowerShell)`
Tell terminal which environment to work in:
`export FLASK_ENV=development (Linux/MacOS/GitBash)`
`set FLASK_ENV=development (Windows Command Prompt)`
`$env:FLASK_ENV="development" (PowerShell)`
once everything is set launch:
`flask run`
