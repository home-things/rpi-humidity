#!/usr/bin/env python3
import time
import board
import adafruit_dht
import sys

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D12)
 
while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        #temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(humidity)
 
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        sys.stderr.write(error.args[0])
 
    time.sleep(2.0)
