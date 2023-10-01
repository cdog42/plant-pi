import os
import time
import subprocess

# Directory to store images
dir_name = '/home/plantpi/programs/timelapse-project/plant-pics'

# Make the directory if it doesn't exist
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

while True:
    # Get the current timestamp for unique file naming
    timestamp = time.strftime('%Y%m%d%H%M%S')
    filename = f"{dir_name}/plant_{timestamp}.jpg"

    # Capture the image using fswebcam from /dev/video0
    try:
        subprocess.run(['fswebcam', '-d', '/dev/video0', '-r', '1920x1080', '--no-banner', filename], check=True)
        print(f"Image saved as {filename}")
    except subprocess.CalledProcessError:
        print("Error capturing image!")

    # Wait for 10 minutes
    time.sleep(60)
