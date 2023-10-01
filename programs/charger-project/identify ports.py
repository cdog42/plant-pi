import pyudev
from datetime import datetime, timedelta
import os
import time

PORT_MAPPINGS_FILE = "port_mappings.txt"

def load_port_mappings():
    """Load port mappings from file."""
    if not os.path.exists(PORT_MAPPINGS_FILE):
        return {}
    with open(PORT_MAPPINGS_FILE, "r") as f:
        mappings = {}
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 2:
                mappings[parts[0]] = parts[1]
        return mappings

def save_port_mapping(port, name):
    """Save port to name mapping in file."""
    with open(PORT_MAPPINGS_FILE, "a") as f:
        f.write(f"{port},{name}\n")

def get_usb_port_info(device):
    """Extracts the bus and port information from a udev USB device."""
    usb_device = device.find_parent('usb', 'usb_device')
    if usb_device:
        busnum = usb_device.attributes.get('busnum').decode('utf-8')
        devpath = usb_device.attributes.get('devpath').decode('utf-8')
        return f"USB Bus {busnum} {devpath}"
    return None

def main():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')
    
    port_mappings = load_port_mappings()

    last_event_time = None
    last_port_info = None

    for device in iter(monitor.poll, None):
        if device.action == "remove":
            current_port_info = get_usb_port_info(device)

            # Check if we're seeing a second unplugged event shortly after the first
            if (last_event_time and
                current_port_info == last_port_info and 
                datetime.now() - last_event_time < timedelta(seconds=1)):
                # Ignore the previous event
                last_event_time = None
                last_port_info = None
                continue

            # If we've detected a previous event and there wasn't another one shortly after
            if last_event_time and datetime.now() - last_event_time >= timedelta(seconds=1):
                if last_port_info not in port_mappings:
                    port_name = input(f"Enter a name for {last_port_info}: ")
                    save_port_mapping(last_port_info, port_name)
                    port_mappings[last_port_info] = port_name
                    print(f"Saved mapping: {last_port_info} -> {port_name}")

            # Update the last_event_time and last_port_info
            last_event_time = datetime.now()
            last_port_info = current_port_info

            # Short sleep to check for a subsequent unplugged event
            time.sleep(0.5)

if __name__ == "__main__":
    main()
