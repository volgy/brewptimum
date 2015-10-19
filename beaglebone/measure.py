#!/usr/bin/env python

import sys
import time
import os
import glob

def check_w1():
    if not os.path.isdir('/sys/devices/w1_bus_master1'):
        print >> sys.stderr, '1-wire master is not enabled, trying to activate...'
        #f = open('/sys/devices/bone_capemgr.9/slots', 'w')
        #print >> f, 'w1'
        #f.close()
        os.system("sudo sh -c 'echo w1 > /sys/devices/bone_capemgr.9/slots'")
	time.sleep(2)

def get_temp():
    for d in glob.glob('/sys/devices/w1_bus_master1/28-*'):
        with open(os.path.join(d, 'w1_slave'), 'r') as f:
            print f.readlines()

if __name__ == '__main__':
    check_w1()
    get_temp()
    print time.strftime('%Y/%m/%d %H:%M:%S')

