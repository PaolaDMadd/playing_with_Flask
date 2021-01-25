from flask import Flask


app = Flask(__name__)
# CORS(app)

from app import db 
from app import routes