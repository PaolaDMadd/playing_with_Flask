from app import app
from flask import Flask, g, jsonify, request
from controllers import trainers
from app.db import get_db

@app.route('/')
def home():
    return jsonify({'message': 'Hello from App.py!'}), 200


@app.route('/api/trainers/', methods=['GET'])
def trainer_index():
    resp, code =  trainers.index(request)
    return jsonify(resp), code



@app.route('/api/trainers/<int:trainers_id>', methods=['GET'])
def shoe_handler(trainers_id):
    fns = {
        'GET': trainers.show
        # 'PATCH': trainers.update,
        # 'PUT': trainers.update,
        # 'DELETE': trainers.destroy
    }
    resp, code = fns[request.method](request, trainers_id)
    return jsonify(resp), code
