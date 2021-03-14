#!/usr/bin/python

# Christoph Franke
# mail@cfranke.org
# 14.03.2020

import socket
import argparse
import time
import datetime

color_red = '\033[91m'
color_green = '\033[92m'
color_norm = '\033[0m'

def checkPort(ip, port, timeout):
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result = s.connect((ip, port))
        s.shutdown(1)
        
        if (color=="True"):
            print (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+"   "+str(target)+":"+str(port)+color_green+"   OPEN"+color_norm)
        else:
            print (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+"   "+str(target)+":"+str(port)+"   OPEN")
    except: 
        if (color=="True"):
            print (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+"   "+str(target)+":"+str(port)+color_red+"   CLOSED"+color_norm)
        else:
            print (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+"   "+str(target)+":"+str(port)+"   CLOSED")

parser = argparse.ArgumentParser(description='TCPing')
parser.add_argument('-t','--target',help='Hostname or IPv4 address', required=True)
parser.add_argument('-p','--port',help='Port', required=True)
parser.add_argument('-c', '--color', help='Color Output', default=True)
parser.add_argument('-T', '--timeout', help='timeout', default=0.5)
args = vars(parser.parse_args())


target = str(args['target'])
port = str(args['port'])
color = str(args['color'])
timeout = float(args['timeout'])

print ("""
 _             _             
| |_ ___ _ __ (_)_ __   __ _ 
| __/ __| '_ \| | '_ \ / _` |
| || (__| |_) | | | | | (_| |
 \__\___| .__/|_|_| |_|\__, |
        |_|            |___/ 
""")

print("")
print("--------------------------------------------------")
print("   TARGET: "+str(target))
print(" TCP PORT: "+str(port))
print("  TIMEOUT: "+str(timeout)+" seconds")
print("    COLOR: "+str(color))
print("--------------------------------------------------")
print("")

try:
    while True:
        checkPort(str(target), int(port), float(timeout))
        time.sleep(1)
except KeyboardInterrupt:
    print('\n*** Stopped ***')
