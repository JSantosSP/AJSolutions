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

@app.route('/api/crearu/<crearu_id>', methods=['GET'])
def getUu(crearu_id):
    d = db.user.find_one({"_id": ObjectId(crearu_id)})
    item = {
         'id': str(d['_id']),
            'nombre': d['nombre'],
            'apell': d['apell'],
            'tel': d['tel'],
            'mail': d['mail'],
            'direc': d['direc'],
            'cp': d['cp'],
            'Nu': d['Nu'],
            'pw': d['pw'],
            'T': d['T']
    }

    return jsonify(data=item), 200

@app.route('/api/crearpd/<crearpd_id>', methods=['GET'])
def getPd(crearpd_id):
    d = db.pedido.find_one({"_id": ObjectId(crearpd_id)})
    item = {
        'id': str(d['_id']),
        'id_pz': d['id_pz'],
        'id_us': d['id_us'],
        'unid': d['unid'],
        'mat': d['mat'],
        'tp_imp': d['tp_imp']
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
            'direc': d['direc'],
            'cp': d['cp'],
            'Nu': d['Nu'],
            'pw': d['pw'],
            'T': d['T']
        }
        data.append(item)

    return jsonify(data=data), 200

@app.route('/api/crearpd', methods=['GET'])
def getPdu():
    _todos = db.pedido.find()
    item = {}
    data = []
    for d in _todos:
        item = {
            'id': str(d['_id']),
            'id_pz': d['id_pz'],
            'id_us': d['id_us'],
            'unid': d['unid'],
            'mat': d['mat'],
            'tp_imp': d['tp_imp']
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
        'direc': data['direc'],
        'cp': data['cp'],
        'Nu': data['Nu'],
        'pw': data['pw'],
        'T': data['T']
    }
    db.user.insert_one(item)

    return jsonify(data=data), 201

@app.route('/api/crearpd', methods=['POST'])
def createPd():
    data = request.get_json(force=True)
    item = {
        'id_pz': data['id_pz'],
        'id_us': data['id_us'],
        'unid': data['unid'],
        'mat': data['mat'],
        'tp_imp': data['tp_imp']
    }
    db.pedido.insert_one(item)

    return jsonify(data=data), 201

@app.route('/api/crearp/<crearp_id>', methods=['PATCH'])
def updateP(crearp_id):
    data = request.get_json(force=True)
    db.piezas.update_one({"_id": ObjectId(crearp_id)}, {"$set": data})

    return jsonify(data=data), 204

@app.route('/api/crearu/<crearu_id>', methods=['PATCH'])
def updateU(crearu_id):
    data = request.get_json(force=True)
    db.user.update_one({"_id": ObjectId(crearu_id)}, {"$set": data})

    return jsonify(data=data), 204

@app.route('/api/crearpd/<crearpd_id>', methods=['PATCH'])
def updatePd(crearpd_id):
    data = request.get_json(force=True)
    db.pedido.update_one({"_id": ObjectId(crearpd_id)}, {"$set": data})

    return jsonify(data=data), 204

@app.route('/api/deletep/<deletep_id>', methods=['DELETE'])
def deleteP(deletep_id):
    db.piezas.delete_one({"_id": ObjectId(deletep_id)})

    return jsonify(), 204

@app.route('/api/deleteu/<deleteu_id>', methods=['DELETE'])
def deleteU(deleteu_id):
    db.user.delete_one({"_id": ObjectId(deleteu_id)})

    return jsonify(), 204

@app.route('/api/deletepd/<deletepd_id>', methods=['DELETE'])
def deletePd(deletepd_id):
    db.pedido.delete_one({"_id": ObjectId(deletepd_id)})

    return jsonify(), 204


if __name__ == "__main__":
    ENVIRONMENT_DEBUG = environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = environ.get("APP_PORT", 5000)
    app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
