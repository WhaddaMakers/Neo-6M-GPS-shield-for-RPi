#!/usr/bin/python3

"""
@@@@@@@@@@@@@@@@@@@@@@                                                                                                                               
@@@@@@@@@@@@@@@@@@@@@@             @@@.    @@@    @@@.     @@@@    @@@@        @@@@@@@@@        @@@@@@@@@@@@@.     .@@@@@@@@@@@@@        @@@@@@@@@  
@@@@@%%@@@%%@@@%%@@@@@             @@@@    @@@    @@@@     @@@@    @@@@       @@@@@@@@@@        @@@@@@@@@@@@@@     @@@@@@@@@@@@@@        @@@@@@@@@  
@@@@@  @@@  @@@  @@@@@             @@@@    @@@    @@@@     @@@@    @@@@       @@@@   @@@@        @@@@@   @@@@@       @@@@@   @@@@       @@@@   @@@@ 
@@@@@            @@@@@             @@@@   @@@@    @@@@     @@@@@@@@@@@@       @@@@   @@@@        @@@@@   @@@@@       @@@@@   @@@@       @@@@   @@@@ 
@@@@@   @    @   @@@@@             @@@@   @@@@    @@@@     @@@@@@@@@@@@       @@@@@@@@@@@        @@@@@   @@@@@       @@@@@   @@@@       @@@@@@@@@@@ 
@@@@@            @@@@@             @@@@###@@@@@##@@@@@     @@@@    @@@@      @@@@@@@@@@@@       #@@@@@###@@@@@     ##@@@@@###@@@@       @@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@             @@@@@@@@@@@@@@@@@@@     @@@@    @@@@      @@@@    @@@@@      @@@@@@@@@@@@@@     @@@@@@@@@@@@@@      @@@@     @@@@
@@@@@@@@@@@@@@@@@@@@@@

Example code for Whadda NEO-6M GPS shield for RPi

Description:
  This example shows you how you can use the GPS data from the GPS module in your own python scripts.
  The example python file prints the current GPS position (latitude, longitude), time and the number of satellites in sight.

Required software:
  - gpsd and gpsd-client
  - gpsd-py3
  
Code inspired by gpsd-py3 example code (https://github.com/MartijnBraam/gpsd-py3)
Author: Midas Gossye
(c) 2021 Whadda, premium makers brand by Velleman
"""

import gpsd
import time
from datetime import datetime

running = True

# Connect to the local gpsd server
gpsd.connect()


try: 
    while running:
        
        packet = gpsd.get_current() # Get latest gps data packet from gpsd

        try: 
            print() # print blank line
            print("Number of sats in sight: {}".format(packet.sats)) # Print number of sats in sight
            pos = packet.position() # Get position
            print("Location (lat,lon): {}".format(pos)) # Print position

            raw_time_str = packet.time # Get raw time string
            time_data = raw_time_str.split(".")[0] # Split time string at . , only use first half
            gps_time = datetime.strptime(time_data, "%Y-%m-%dT%H:%M:%S") # Convert time string to datetime object

            print("GPS UTC Time: {}".format(gps_time.strftime("%H:%M:%S %Y-%m-%d"))) # Print GPS time in HH:MM:SS YYYY-MM-DD format
        except gpsd.NoFixError:
            print("No fix...") # If no fix...

        time.sleep(1)  
        
# Stop running program when user entered ctrl-c
except KeyboardInterrupt:
    running = False


