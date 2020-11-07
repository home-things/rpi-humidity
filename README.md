DHT22 rpi wrapper

# Start
```sh
#
# 0. upgrade raspbian to buster or later
sudo su
vim /etc/apt/source.list
apt-get remove apt-listchanges
apt update && apt dist-upgrade -y
apt autoremove -y
apt autoclean
reboot


#
# 1. clone
mkdir -p ~/services/humidity && cd ~/services/humidity
git clone .


#
# 2. create python3 virtual env and deps
sudo apt-get install python3-venv
python3 -m venv env
./pip3-install-requirements
# original instructions:
# 1. https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup
# 2. https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi


#
# 3. run python env
source env/bin/activate


#
# 4. add data collector to cron (crontab -e):
@reboot cd /home/pi/services/humidity/ && ./start-logging >> log

# WARNING. it'll generate more errors and sometimes will append new humidity value into log file. It's normal...
```

# Request
It takes 3 latest values and produces its avg
```sh
~/services/humidity/get-humidity # 25.11
```
