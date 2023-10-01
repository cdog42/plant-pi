#!/usr/bin/env python3

import os
import time
import subprocess
import fcntl
import sys
from PIL import Image  # Import the necessary module


lock_file_path = '/home/plantpi/programs/timelapse-project/take-picture.py.lock'

# Try to acquire a lock
lock_file = open(lock_file_path, 'w')
try:
    fcntl.lockf(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
except IOError:
    print("Another instance of this script is already running.")
    sys.exit(1)

# ... rest of your script ...

# At the end, you can close the lock file
lock_file.close()


# Directory to store images
dir_name = '/home/plantpi/programs/timelapse-project/plant-pics'

# Make the directory if it doesn't exist
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

while True:
    # Get the current timestamp for unique file naming
    timestamp = time.strftime('%Y-%m-%d_%H-%M')
    filename = f"{dir_name}/plant_{timestamp}.jpg"


    # Temporary filename to store image before rotation
    temp_filename = f"{dir_name}/temp_{timestamp}.jpg"

    # Capture the image using fswebcam from /dev/video0
    try:
        subprocess.run(['fswebcam', '-d', '/dev/video0', '-r', '1920x1080', '--no-banner', temp_filename], check=True)
        
        # Rotate the image
        with Image.open(temp_filename) as img:
            rotated_img = img.rotate(90, expand=True)
            rotated_img.save(filename)

        # Delete the temporary file
        os.remove(temp_filename)

        print(f"Image saved as {filename}")
    except (subprocess.CalledProcessError, Exception) as e:
        print(f"Error capturing or rotating image! {e}")

    # Wait for 10 minutes
    time.sleep(600)

lock_file.close()
