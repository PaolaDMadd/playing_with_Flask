import sqlite3
import click
from app import app
from flask import current_app, g
from flask.cli import with_appcontext

# below if there is no local file named flask_trainers it will creates one.
DATABASE = 'flask_trainers.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = sqlite3.connect(DATABASE)
        db = g._database
    return db


def init_db():
    """Clear existing data and create new tables."""
    db = get_db()
    with current_app.open_resource("seeds.sql") as f:
        db.executescript(f.read().decode("utf8"))

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database')

app.cli.add_command(init_db_command)

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()


# def close_db(e=None):
#     db = g.pop('db', None)

#     if db is not None:
#         db.close()