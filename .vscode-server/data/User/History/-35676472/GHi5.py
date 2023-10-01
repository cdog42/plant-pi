#!/usr/bin/env python3

import requests
import time
import sqlite3
from datetime import datetime

ESP32_URL = "http://esp32-moisture.local/data"
DB_FILENAME = "/home/plantpi/programs/sensor-project/sensor_data.db"



def setup_database():
    conn = sqlite3.connect(DB_FILENAME)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sensor_data (
        id INTEGER PRIMARY KEY,
        timestamp TEXT NOT NULL,
        moisture_1 REAL NOT NULL,
        moisture_2 REAL NOT NULL
    )
    ''')

    conn.commit()
    conn.close()


setup_database()  # Ensure the table exists before the loop starts

# Maintain an open connection
conn = sqlite3.connect(DB_FILENAME)
cursor = conn.cursor()

try:
    while True:
        try:
            response = requests.get(ESP32_URL)
            data = response.json()

            moisture_1 = data['moisture-1']
            moisture_2 = data['moisture-2']

            print(f"Moisture-1 Value: {moisture_1}, Moisture-2 Value: {moisture_2}")

            # Insert data into the SQLite database
            cursor.execute("INSERT INTO sensor_data (timestamp, moisture_1, moisture_2) VALUES (?, ?, ?)", 
                           (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), moisture_1, moisture_2))
            conn.commit()

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from ESP32: {e}")

        time.sleep(30)  # Check every 5 seconds

finally:
    # If the script ends or there's an issue, close the connection
    conn.close()
