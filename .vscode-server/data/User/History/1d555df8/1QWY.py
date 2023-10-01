import pyudev
from datetime import datetime
import re
import csv
import os

# Define the unwanted port labels in this list
unwanted_port_labels = ["USB Bus 1 1.1.1", "USB Bus 1 1.1"]  # Add more as needed

# ... [rest of your code remains unchanged up until the write_to_log and process_and_clean_log functions] ...

def write_to_log(port_label, time_plugged_in, time_unplugged, total_time_plugged_in):
    log_path = "/home/plantpi/programs/charger-project/Charge Log.csv"  # <--- Absolute path
    if port_label in port_label_mapping:
        port_label = port_label_mapping[port_label]  # Change to the friendly name
        with open(log_path, "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([port_label, time_plugged_in, time_unplugged, total_time_plugged_in])
    else:
        print(f"Port label not found in mapping: {port_label}")

def process_and_clean_log(port_label, time_plugged_in, time_unplugged, total_time_plugged_in):
    log_path = "/home/plantpi/programs/charger-project/Charge Log.csv"  # <--- Absolute path
    with open(log_path, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([port_label, time_plugged_in, time_unplugged, total_time_plugged_in])

    with open(log_path, 'r', newline='') as f:
        reader = csv.reader(f)
        original_rows = list(reader)

    cleaned_rows = []
    for row in original_rows:
        if row[0] not in unwanted_port_labels:
            row[0] = port_label_mapping.get(row[0], row[0])
            cleaned_rows.append(row)

    with open(log_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(cleaned_rows)

# ... [rest of your code remains unchanged] ...

def initialize_csv():
    log_path = "/home/plantpi/programs/charger-project/Charge Log.csv"  # <--- Absolute path
    if not os.path.exists(log_path):
        with open(log_path, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Port Label", "Time Plugged In", "Time Unplugged", "Total Time Plugged In"])

if __name__ == "__main__":
    initialize_csv()
    main()
