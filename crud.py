from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from ua.lviv.iot.python.models.machinery import Machinery
import os
import json
import copy

with open('secret.json') as f:
    SECRET = json.load(f)

auth_plugin = 'mysql_native_password'

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Machine(Machinery, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year_of_production = db.Column(db.Integer, unique=False)
    weight_of_machinery_in_kg = db.Column(db.Integer, unique=False)
    machine_mileage = db.Column(db.Integer, unique=False)
    wheel_type = db.Column(db.String(32), unique=False)
    fuel_type = db.Column(db.String(32), unique=False)
    height_of_machinery = db.Column(db.Integer, unique=False)
    model_of_machinery = db.Column(db.String(32), unique=False)

    def __init__(self, year_of_production=0, lose_fuel_per_one_hour=0,
                 weight_of_machinery_in_kg=0, machine_mileage=0,
                 wheel_type="4x4", fuel_type="petrol",
                 height_of_machinery=0, model_of_machinery="mersedes"):
        super().__init__(year_of_production, lose_fuel_per_one_hour,
                         weight_of_machinery_in_kg, machine_mileage,
                         wheel_type, fuel_type)
        self.height_of_machinery = height_of_machinery
        self.model_of_machinery = model_of_machinery


class Machine(ma.Schema):
    class Meta:
        fields = ('year_of_production', 'lose_fuel_per_one_hour',
                  'weight_of_machinery_in_kg', 'machine_mileage', 'wheel_type',
                  'fuel_type', 'height_of_machinery',
                  'model_of_machinery')


machine_schema = Machine()
machines_schema = Machine(many=True)


@app.route("/machine", methods=["POST"])
def add_machine():
    year_of_production = request.json['year_of_production']
    lose_fuel_per_one_hour = request.json['lose_fuel_per_one_hour']
    weight_of_machinery_in_kg = request.json['weight_of_machinery_in_kg']
    machine_mileage = request.json['machine_mileage']
    wheel_type = request.json['wheel_type']
    fuel_type = request.json['fuel_type']
    height_of_machinery = request.json['height_of_machinery']
    model_of_machinery = request.json['model_of_machinery']
    machine = Machine(year_of_production,
                      lose_fuel_per_one_hour,
                      weight_of_machinery_in_kg,
                      machine_mileage,
                      wheel_type,
                      fuel_type,
                      height_of_machinery,
                      model_of_machinery)
    db.session.add(machine)
    db.session.commit()
    return machine_schema.jsonify(machine)


@app.route("/machine", methods=["GET"])
def get_machine():
    all_machine = Machine.query.all()
    result = machines_schema.dump(all_machine)
    return jsonify({'machines': result})


@app.route("/machine/<id>", methods=["GET"])
def machine_detail(id):
    machine = Machine.query.get(id)
    if not machine:
        abort(404)
    return machine_schema.jsonify(machine)


@app.route("/machine/<id>", methods=["PUT"])
def machine_update(id):
    machine = Machine.query.get(id)
    if not machine:
        abort(404)
    old_machine = copy.deepcopy(machine)
    machine.year_of_production = request.json['year_of_production']
    machine.lose_fuel_per_one_hour = request.json['lose_fuel_per_one_hour']
    machine.weight_of_machinery_in_kg = request.json['weight_of_machinery_in_kg']
    machine.machine_mileage = request.json['machine_mileage']
    machine.wheel_type = request.json['wheel_type']
    machine.fuel_type = request.json['fuel_type']
    machine.height_of_machinery = request.json['height_of_machinery']
    machine.model_of_machinery = request.json['model_of_machinery']
    db.session.commit()
    return machine_schema.jsonify(old_machine)


@app.route("/machine/<id>", methods=["DELETE"])
def machine_delete(id):
    machine = Machine.query.get(id)
    if not machine:
        abort(404)
    db.session.delete(machine)
    db.session.commit()
    return machine_schema.jsonify(machine)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
