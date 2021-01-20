#!/bin/bash 
pipenv install -r requirements.txt
pipenv shell

export FLASK_APP=server.py
export FLASK_ENV=development

flask run