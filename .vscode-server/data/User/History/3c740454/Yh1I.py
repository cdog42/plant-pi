#!/usr/bin/env python3

from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import datetime
import random
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/plantpi/programs/sensor-project/sensor_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Silence the deprecation warning
db = SQLAlchemy(app)

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(50))
    moisture_1 = db.Column(db.Float)
    moisture_2 = db.Column(db.Float)

def setup_database():
    with app.app_context():  # ensure we're in an app context
        db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    records = SensorData.query.all()
    return jsonify([
        {
            'timestamp': record.timestamp,
            'moisture-1': record.moisture_1,
            'moisture-2': record.moisture_2
        } for record in records
    ])

@app.route('/data/<start_date>/<end_date>')
def get_data_range(start_date, end_date):
    records = SensorData.query.filter(SensorData.timestamp.between(start_date, end_date)).all()
    return jsonify([
        {
            'timestamp': record.timestamp,
            'moisture-1': record.moisture_1,
            'moisture-2': record.moisture_2
        } for record in records
    ])


if __name__ == '__main__':
    setup_database()  # Ensure the database and tables are created before starting the app
    app.run(debug=True, host='0.0.0.0')
