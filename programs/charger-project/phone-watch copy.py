

import pyudev
from datetime import datetime
import re
import csv
import os

# Define the unwanted port labels in this list
unwanted_port_labels = ["USB Bus 1 1.1.1","USB Bus 1 1.1"]  # Add more as needed

# Define a mapping of unfriendly port labels to friendly names
port_label_mapping = {
    "USB Bus 1 1.1.1.4": "Dad",
    "USB Bus 1 1.1.1.3": "Hudson",
    "USB Bus 1 1.1.1.2": "Meadow",
    "USB Bus 1 1.1.1.1": "Spare1",
    "USB Bus 1 1.1.4": "Spare2",
    "USB Bus 1 1.1.3":"Spare3",
    "USB Bus 1 1.1.2":"Spare4"
    # Add more mappings as needed
}

def clean_csv_file(filename):
    # Read the original rows
    with open(filename, 'r', newline='') as f:
        reader = csv.reader(f)
        original_rows = list(reader)

    # Filter rows and replace unfriendly port labels
    cleaned_rows = []
    for row in original_rows:
        if row[0] not in unwanted_port_labels:
            # Replace the port label if a friendly name is defined
            row[0] = port_label_mapping.get(row[0], row[0])
            cleaned_rows.append(row)

    # Write the cleaned rows back to the CSV file
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(cleaned_rows)


def write_to_log(port_label, time_plugged_in, time_unplugged, total_time_plugged_in):
    with open("Charge Log.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([port_label, time_plugged_in, time_unplugged, total_time_plugged_in])


def process_and_clean_log(port_label, time_plugged_in, time_unplugged, total_time_plugged_in):
    # Write the new log entry
    with open("Charge Log.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([port_label, time_plugged_in, time_unplugged, total_time_plugged_in])

    # Read the rows for cleaning
    with open("Charge Log.csv", 'r', newline='') as f:
        reader = csv.reader(f)
        original_rows = list(reader)

    print("Original Rows:", original_rows)  # Debugging print

    # Filter rows and replace unfriendly port labels
    cleaned_rows = []
    for row in original_rows:
        if row[0] not in unwanted_port_labels:
            # Replace the port label if a friendly name is defined
            row[0] = port_label_mapping.get(row[0], row[0])
            cleaned_rows.append(row)

    print("Cleaned Rows:", cleaned_rows)  # Debugging print

    # Write the cleaned rows back to the CSV file
    with open("Charge Log.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(cleaned_rows)



class USBDevice:
    def __init__(self, device_name, sys_path, port_label):
        self.device_name = device_name
        self.sys_path = sys_path
        self.port_label = port_label
        self.plug_in_time = datetime.now()

    def get_time_plugged_in(self):
        return datetime.now() - self.plug_in_time


# Define a mapping for the port paths to their labels
port_label_mapping = {
    "1.1929": "USB PORT 1"
    # You can add more mappings as needed
}


def get_usb_port_info(device):
    """Extracts the bus and port information from a udev USB device."""
    usb_device = device.find_parent('usb', 'usb_device')
    if usb_device:
        busnum = usb_device.attributes.get('busnum').decode('utf-8')
        devpath = usb_device.attributes.get('devpath').decode('utf-8')
        port_label = port_label_mapping.get(devpath, devpath)
        return f"USB Bus {busnum} {port_label}"
    return "Unknown Port"


def main():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')

    plugged_in_devices = {}

    for device in iter(monitor.poll, None):
        port_info = get_usb_port_info(device)
        device_name = device.get("DEVNAME", "Unknown Device")

        if device.action == "add":
            plugged_in_devices[device_name] = USBDevice(device_name, device.sys_path, port_info)
        elif device.action == "remove" and device_name in plugged_in_devices:
            usb_device = plugged_in_devices[device_name]
            time_plugged_in_str = usb_device.plug_in_time.strftime('%Y-%m-%d %H:%M:%S')
            time_unplugged_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            total_time_plugged_in_str = str(usb_device.get_time_plugged_in())
            
            process_and_clean_log(usb_device.port_label, time_plugged_in_str, time_unplugged_str, total_time_plugged_in_str)
            del plugged_in_devices[device_name]
           

# Add this function to your code
def initialize_csv():
    if not os.path.exists("Charge Log.csv"):
        with open("Charge Log.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Port Label", "Time Plugged In", "Time Unplugged", "Total Time Plugged In"])

# And call it before your main function
if __name__ == "__main__":
    initialize_csv()
    main()