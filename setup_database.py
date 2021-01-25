# import sqlite3

# import click
# from flask import current_app, g
# from flask.cli import with_appcontext

# # def init_db():
# #     with server.app_context():
# #         db = get_db()
# #         with server.open_resource('seeds.sql', mode='r') as f:
# #             db.cursor().executescript(f.read())
# #             for row in db.execute('SELECT * FROM trainers;'):
# #                 print(row)
# #         db.commit()

# def get_db():
#     if 'db' not in g:
#         g.db = sqlite3.connect(
#             current_app.config['DATABASE'],
#             detect_types=sqlite3.PARSE_DECLTYPES
#         )
#         g.db.row_factory = sqlite3.Row

#     return g.db


# def close_db(e=None):
#     db = g.pop('db', None)

#     if db is not None:
#         db.close()