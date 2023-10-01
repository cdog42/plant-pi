sudo apt-get update
sudo apt-get install openssh-server
sudo raspi-config
sudo apt-get install openssh-server
sudo adduser pi
sudo usermod -aG sudo pi
sudo apt update
sudo apt upgrade
sudo timedatectl set-ntp true
timedatectl status
sudo raspi-config
sudo systemctl status vncserver-x11-serviced.service
sudo systemctl start vncserver-x11-serviced.service
sudo apt-get purge realvnc-vnc-server
sudo apt-get install realvnc-vnc-server
sudo reboot
sudo usermod -o -u 0 piD
sudo usermod -o -u 0 pi
ps -u pi
who
who:
sudo usermod -o -u 0 pi
sudo kill -9 1084
sudo usermod -o -u 0 pi
sudo kill -9 1166
sudo usermod -o -u 0 pi
sudo kill -9 1176
sudo usermod -o -u 0 pi
sudo kill -9 1471
sudo usermod -o -u 0 pi
sudo kill -9 2589
sudo usermod -o -u 0 pi
sudo kill -9 2591
sudo usermod -o -u 0 pi
sudo kill -9 2615
sudo usermod -o -u 0 pi
#!/bin/bash
# Check if the script is run as root
if [ "$(id -u)" -ne 0 ]; then     echo "This script must be run as root.";     exit 1; fi
/bin/python /home/plantpi/programs/timelapse-project/take-picture.py
pip install Pillow
/bin/python /home/plantpi/programs/timelapse-project/take-picture.py
/bin/python /home/plantpi/programs/sensor-project/web-interface.py
pip3 install flask_sqlalchemy
/bin/python /home/plantpi/programs/sensor-project/web-interface.py
/bin/python /home/plantpi/programs/sensor-project/data-reader.py
/bin/python /home/plantpi/programs/charger-project/phone-watch.py
pip3 install pyudev
/bin/python /home/plantpi/programs/charger-project/phone-watch.py
/bin/python /home/pi/programs/timelapse-project/take-picture.py
sudo usermod -o -u 0 pi
sudo kill -9 2755
sudo usermod -o -u 0 pi
sudo passwd pi
usermod -u 1000 pi
usermod -u 1001 pi
sudo usermod -u 1001 pi
sudo kill -9 1
sudo usermod -u 1001 pi
sudo kill -9 1
sudo usermod -u 1001 pi
/bin/python /home/plantpi/programs/sensor-project/web-interface.py
/bin/python /home/plantpi/programs/sensor-project/data-reader.py
/bin/python /home/plantpi/programs/timelapse-project/take-picture.py
chmod +x /home/plantpi/programs/charger-project/charger0project.py
chmod +x /home/plantpi/programs/charger-project/phone-watch.py
chmod +x /home/plantpi/programs/sensor-project/web-interface.py
chmod +x /home/plantpi/programs/sensor-project/data-reader.py
chmod +x /home/plantpi/programs/timelapse-project/take-picture.py
sudo nano /etc/rc.local
sudo reboot
