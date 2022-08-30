from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, ObjectId
from os import environ

app = Flask(__name__)
app.config["MONGO_URI"] = environ.get("MONGO_URI")
mongo = PyMongo(app)
db = mongo.db


@app.route('/api/crearp/<crearp_id>', methods=['GET'])
def getPp(crearp_id):
    d = db.piezas.find_one({"_id": ObjectId(crearp_id)})
    item = {
        'id': str(d['_id']),
            'nombre': d['nombre'],
            'precio': d['precio'],
            'desc': d['desc']
    }

    return jsonify(data=item), 200


@app.route('/api/crearp', methods=['GET'])
def getP():
    _todos = db.piezas.find()
    item = {}
    data = []
    for d in _todos:
        item = {
            'id': str(d['_id']),
            'nombre': d['nombre'],
            'precio': d['precio'],
            'desc': d['desc']
        }
        data.append(item)

    return jsonify(data=data), 200

@app.route('/api/crearu', methods=['GET'])
def getU():
    _todos = db.user.find()
    item = {}
    data = []
    for d in _todos:
        item = {
            'id': str(d['_id']),
            'nombre': d['nombre'],
            'apell': d['apell'],
            'tel': d['tel'],
            'mail': d['mail'],
            'direc': d['direc']
        }
        data.append(item)

    return jsonify(data=data), 200


@app.route('/api/crearp', methods=['POST'])
def createTodo():
    data = request.get_json(force=True)
    item = {
        'nombre': data['nombre'],
        'precio': data['precio'],
        'desc': data['desc']
    }
    db.piezas.insert_one(item)

    return jsonify(data=data), 201

@app.route('/api/crearu', methods=['POST'])
def createU():
    data = request.get_json(force=True)
    item = {
        'nombre': data['nombre'],
        'apell': data['apell'],
        'tel': data['tel'],
        'mail': data['mail'],
        'direc': data['direc']
    }
    db.user.insert_one(item)

    return jsonify(data=data), 201

@app.route('/api/todo/<todo_id>', methods=['PATCH'])
def updateP(todo_id):
    data = request.get_json(force=True)
    db.todo.update_one({"_id": ObjectId(todo_id)}, {"$set": data})

    return jsonify(data=data), 204


@app.route('/api/deletep/<deletep_id>', methods=['DELETE'])
def deleteTodo(deletep_id):
    db.piezas.delete_one({"_id": ObjectId(deletep_id)})

    return jsonify(), 204


if __name__ == "__main__":
    ENVIRONMENT_DEBUG = environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = environ.get("APP_PORT", 5000)
    app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
