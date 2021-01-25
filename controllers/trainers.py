''' Shoes controller '''
from werkzeug.exceptions import BadRequest
from flask import Flask, g, jsonify, request
from app.db import get_db


def index(req):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM trainers")
    trainers = cursor.fetchall()
    return trainers, 200
   

def show(req, uid):
    trainers = find_by_uid(uid)
    if trainers is None:
        return f"We don't have that brand with id {uid}!", 404
    else:
        return trainers, 200


# def create(req):
#     new_cat = req.get_json()
#     new_cat['id'] = sorted([c['id'] for c in cats])[-1] + 1
#     cats.append(new_cat)
#     return new_cat, 201

# def update(req, uid):
#     cat = find_by_uid(uid)
#     data = req.get_json()
#     print(data)
#     for key, val in data.items():
#         cat[key] = val
#     return cat, 200

# def destroy(req, uid):
#     cat = find_by_uid(uid)
#     cats.remove(cat)
#     return cat, 204

def find_by_uid(uid):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM trainers WHERE id = {uid}")
    return cursor.fetchone()