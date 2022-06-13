#!/usr/bin/python

import time
import sys
from sd_wan import SdWan

if len(sys.argv) < 4:
    print("Please provide host, username and password")
    exit()

HOST = sys.argv[1]
USERNAME = sys.argv[2]
PASSWORD = sys.argv[3]
BASE_URL = f'https://{HOST}/'

def main():
    sdwan_obj = SdWan(BASE_URL, USERNAME, PASSWORD)
    devices = sdwan_obj.get_devices()
    for device in devices:
        try:
            result = sdwan_obj.migrate_device(device)
            print(device["serialNumber"], " " ,result)
        except AssertionError:
            print(f'Device {device["deviceModel"]} not eligible for migration.')
        time.sleep(1)

main()
