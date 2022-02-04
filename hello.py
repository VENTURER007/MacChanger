#!/usr/bin/env python

import subprocess

subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw 34:cf:f6:b8:2a:46", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)
