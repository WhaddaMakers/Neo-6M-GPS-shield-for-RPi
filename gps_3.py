#!/usr/bin/python3

import gpsd
import time
from datetime import datetime

running = True

# Connect to the local gpsd
gpsd.connect()


try: 
    while running:
        # Get gps position
        packet = gpsd.get_current()

        try: 
            print()
            print("Number of sats in sight: {}".format(packet.sats))
            pos = packet.position()
            print("Location (lat,lon): {}".format(pos))

            raw_time_str = packet.time
            time_data = raw_time_str.split(".")[0]
            gps_time = datetime.strptime(time_data, "%Y-%m-%dT%H:%M:%S")

            print("GPS UTC Time: {}".format(gps_time.strftime("%H:%M:%S %Y-%m-%d")))
        except gpsd.NoFixError:
            print("No fix...")

        time.sleep(1)  
        

except KeyboardInterrupt:
    running = False


